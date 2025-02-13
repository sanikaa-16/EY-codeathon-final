
# app/routes/auth.py
from flask import Blueprint, request, jsonify
from ..models.user import User
from .. import db, bcrypt
from ..services.email_service import (
    generate_otp, store_otp, verify_stored_otp, send_otp_email
)

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    try:
        data = request.json
        
        required_fields = ['college_email', 'password', 'role']
        if not all(field in data for field in required_fields):
            return jsonify({'message': 'Missing required fields'}), 400

        if data['role'] not in ['Faculty', 'Student']:
            return jsonify({'message': 'Invalid role. Must be either Faculty or Student'}), 400

        if User.query.filter_by(college_email=data['college_email']).first():
            return jsonify({'message': 'Email already registered!'}), 400
        
        hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
        
        new_user = User(
            college_email=data['college_email'],
            hashed_password=hashed_password,
            role=data['role']
        )
        
        db.session.add(new_user)
        db.session.commit()

        return jsonify({
            'message': 'Sign-Up successful!',
            'user_id': new_user.user_id
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(college_email=data['college_email']).first()

    if user and bcrypt.check_password_hash(user.hashed_password, data['password']):
        return jsonify({
            'message': 'Login successful!',
            'user_id': user.user_id,
            'role': user.role,
            'is_profile_complete': user.is_profile_complete
        })
    return jsonify({'message': 'Invalid credentials!'}), 401

@auth_bp.route('/send-otp', methods=['POST'])
def send_otp():
    try:
        data = request.json
        email = data.get('email')

        if not email:
            return jsonify({'message': 'Email is required'}), 400

        user = User.query.filter_by(college_email=email).first()
        if not user:
            return jsonify({'message': 'User not found'}), 404

        otp = generate_otp()
        store_otp(email, otp)

        if send_otp_email(email, otp):
            return jsonify({'message': 'OTP sent successfully'}), 200
        return jsonify({'message': 'Failed to send OTP'}), 500

    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500

@auth_bp.route('/verify-otp', methods=['POST'])
def verify_otp():
    try:
        data = request.json
        email = data.get('email')
        otp = data.get('otp')

        if not email or not otp:
            return jsonify({'message': 'Email and OTP are required'}), 400

        is_valid, message = verify_stored_otp(email, otp)
        
        if not is_valid:
            return jsonify({'message': message}), 400

        user = User.query.filter_by(college_email=email).first()
        if user:
            return jsonify({
                'message': 'OTP verified successfully',
                'user_id': user.user_id,
                'role': user.role,
                'is_profile_complete': user.is_profile_complete
            }), 200
        
        return jsonify({'message': 'User not found'}), 404

    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500