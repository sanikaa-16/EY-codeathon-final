from flask import Blueprint, request, jsonify
from ..models import Student, Marks, Attendance, User, HoD, Teacher, Dean
from .. import db

student_bp = Blueprint("student", __name__)
dean_bp = Blueprint("dean", __name__)
hod_bp = Blueprint("hod", __name__)
teacher_bp = Blueprint("teacher", __name__)

@student_bp.route("/faculty", methods=["GET"])
def get_faculty():
    student_id = request.args.get("student_id")
    student = Student.query.filter_by(user_id=student_id).first()
    if not student:
        return jsonify({"error": "Unauthorized"}), 403

    faculty = User.query.filter_by(role="teacher", department_id=student.department_id).all()
    return jsonify([{"name": f.college_email, "subject": f.subject} for f in faculty])


@student_bp.route("/marks", methods=["GET"])
def get_marks():
    student_id = request.args.get("student_id")
    student = Student.query.filter_by(user_id=student_id).first()
    if not student:
        return jsonify({"error": "Unauthorized"}), 403

    marks = Marks.query.filter_by(student_id=student.user_id).all()
    return jsonify([{"subject": m.subject, "marks": m.marks_obtained, "max": m.max_marks} for m in marks])


@student_bp.route("/attendance", methods=["GET"])
def get_attendance():
    student_id = request.args.get("student_id")
    student = Student.query.filter_by(user_id=student_id).first()
    if not student:
        return jsonify({"error": "Unauthorized"}), 403

    attendance = Attendance.query.filter_by(student_id=student.user_id).all()
    return jsonify([{"date": a.date.strftime("%Y-%m-%d"), "status": a.status} for a in attendance])


@teacher_bp.route("/students", methods=["GET"])
def get_students():
    teacher_id = request.args.get("teacher_id")
    teacher = Teacher.query.filter_by(user_id=teacher_id).first()
    if not teacher:
        return jsonify({"error": "Unauthorized"}), 403

    students = Student.query.filter_by(teacher_id=teacher.user_id).all()
    return jsonify([{"name": s.college_email, "enrollment": s.enrollment_number} for s in students])


@hod_bp.route("/teachers", methods=["GET"])
def get_teachers():
    hod_id = request.args.get("hod_id")
    hod = HoD.query.filter_by(user_id=hod_id).first()
    if not hod:
        return jsonify({"error": "Unauthorized"}), 403

    teachers = Teacher.query.filter_by(department_id=hod.user_id).all()
    return jsonify([{"name": t.college_email, "subject": t.subject} for t in teachers])


@hod_bp.route("/students", methods=["GET"])
def get_students_hod():
    hod_id = request.args.get("hod_id")
    hod = HoD.query.filter_by(user_id=hod_id).first()
    if not hod:
        return jsonify({"error": "Unauthorized"}), 403

    students = Student.query.filter_by(department_id=hod.user_id).all()
    return jsonify([{"name": s.college_email, "enrollment": s.enrollment_number} for s in students])


@dean_bp.route("/all_data", methods=["GET"])
def get_all_data():
    dean_id = request.args.get("dean_id")
    dean = Dean.query.filter_by(user_id=dean_id).first()
    if not dean:
        return jsonify({"error": "Unauthorized"}), 403

    users = User.query.all()
    return jsonify([{"email": u.college_email, "role": u.role, "salary": u.salary, "phone": u.phone_number} for u in users])
