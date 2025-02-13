import random
import string
import threading
from datetime import datetime, timedelta
from flask_mail import Message
from .. import mail

otp_store = {}
otp_store_lock = threading.Lock()

def generate_otp(length=6):
    return ''.join(random.choices(string.digits, k=length))

def clear_expired_otp(email):
    with otp_store_lock:
        if email in otp_store:
            del otp_store[email]

def store_otp(email, otp, expiry_minutes=10):
    expiry_time = datetime.utcnow() + timedelta(minutes=expiry_minutes)
    
    with otp_store_lock:
        otp_store[email] = {
            'otp': otp,
            'expiry': expiry_time
        }
    
    threading.Timer(expiry_minutes * 60, clear_expired_otp, args=[email]).start()

def verify_stored_otp(email, otp):
    with otp_store_lock:
        if email not in otp_store:
            return False, "OTP not found"
        
        stored_data = otp_store[email]
        if datetime.utcnow() > stored_data['expiry']:
            del otp_store[email]
            return False, "OTP has expired"
        
        if stored_data['otp'] != otp:
            return False, "Invalid OTP"
        
        del otp_store[email]
        return True, "OTP verified successfully"

def send_otp_email(email, otp):
    try:
        msg = Message(
            subject="Your OTP Code",
            recipients=[email],
            body=f"Your OTP code is: {otp}\nThis code will expire in 10 minutes."
        )
        mail.send(msg)
        return True
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return False