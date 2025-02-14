from django.shortcuts import render,HttpResponse, redirect,HttpResponseRedirect
from django.contrib.auth import logout, authenticate, login
from student_management_app.models import CustomUser, Staffs, Students, AdminHOD
from django.contrib import messages

#excel uplaod

import pandas as pd
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from .models import Students, CustomUser, Courses, SessionYearModel
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def my_view(request):
    return HttpResponse("CSRF is disabled for this view.")


def upload_file(request):
    if request.method == "POST" and request.FILES.get("uploaded_file"):
        uploaded_file = request.FILES["uploaded_file"]
        fs = FileSystemStorage()
        file_name = fs.save(uploaded_file.name, uploaded_file)
        file_url = fs.url(file_name)
        return render(request, "hod_template/upload_success.html", {"file_url": file_url})
    return render(request, "hod_template/upload_file.html")

def upload_students_excel(request):
    if request.method == "POST" and request.FILES.get("file"):
        file = request.FILES["file"]
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        file_path = fs.path(filename)

        try:
            df = pd.read_excel(file_path)

            for index, row in df.iterrows():
                try:
                    # Check if course exists
                    course = Courses.objects.filter(id=row["Course ID"]).first()
                    if not course:
                        return JsonResponse({"error": f"Course ID {row['Course ID']} does not exist at row {index + 2}"}, status=400)

                    # Check if session exists
                    session = SessionYearModel.objects.filter(id=row["Session Year ID"]).first()
                    if not session:
                        return JsonResponse({"error": f"Session Year ID {row['Session Year ID']} does not exist at row {index + 2}"}, status=400)

                    # Create user account
                    user = CustomUser.objects.create_user(
                        username=row["Roll Number"],  
                        email=row["Email"],
                        first_name=row["Name"].split()[0],  
                        last_name=" ".join(row["Name"].split()[1:]) if len(row["Name"].split()) > 1 else "",
                        password="defaultpassword123"
                    )

                    # Create student record
                    Students.objects.create(
                        admin=user,
                        gender=row["Gender"],
                        address=row["Address"],
                        course_id=course,
                        session_year_id=session
                    )

                except Exception as row_error:
                    return JsonResponse({"error": f"Error processing row {index + 2}: {str(row_error)}"}, status=400)

            return JsonResponse({"message": "Students uploaded successfully"}, status=201)

        except Exception as e:
            return JsonResponse({"error": f"Unexpected error: {str(e)}"}, status=400)

    return JsonResponse({"error": "Invalid request"}, status=400)
#excel upload

def home(request):
	return render(request, 'home.html')


def contact(request):
	return render(request, 'contact.html')


def loginUser(request):
	return render(request, 'login_page.html')

def doLogin(request):
	
	print("here")
	email_id = request.GET.get('email')
	password = request.GET.get('password')
	# user_type = request.GET.get('user_type')
	print(email_id)
	print(password)
	print(request.user)
	if not (email_id and password):
		messages.error(request, "Please provide all the details!!")
		return render(request, 'login_page.html')

	user = CustomUser.objects.filter(email=email_id, password=password).last()
	if not user:
		messages.error(request, 'Invalid Login Credentials!!')
		return render(request, 'login_page.html')

	login(request, user)
	print(request.user)

	if user.user_type == CustomUser.STUDENT:
		return redirect('student_home/')
	elif user.user_type == CustomUser.STAFF:
		return redirect('staff_home/')
	elif user.user_type == CustomUser.HOD:
		return redirect('admin_home/')

	return render(request, 'home.html')

	
def registration(request):
	return render(request, 'registration.html')
	

def doRegistration(request):
	first_name = request.GET.get('first_name')
	last_name = request.GET.get('last_name')
	email_id = request.GET.get('email')
	password = request.GET.get('password')
	confirm_password = request.GET.get('confirmPassword')

	print(email_id)
	print(password)
	print(confirm_password)
	print(first_name)
	print(last_name)
	if not (email_id and password and confirm_password):
		messages.error(request, 'Please provide all the details!!')
		return render(request, 'registration.html')
	
	if password != confirm_password:
		messages.error(request, 'Both passwords should match!!')
		return render(request, 'registration.html')

	is_user_exists = CustomUser.objects.filter(email=email_id).exists()

	if is_user_exists:
		messages.error(request, 'User with this email id already exists. Please proceed to login!!')
		return render(request, 'registration.html')

	user_type = get_user_type_from_email(email_id)

	if user_type is None:
		messages.error(request, "Please use valid format for the email id: '<username>.<staff|student|hod>@<college_domain>'")
		return render(request, 'registration.html')

	username = email_id.split('@')[0].split('.')[0]

	if CustomUser.objects.filter(username=username).exists():
		messages.error(request, 'User with this username already exists. Please use different username')
		return render(request, 'registration.html')

	user = CustomUser()
	user.username = username
	user.email = email_id
	user.password = password
	user.user_type = user_type
	user.first_name = first_name
	user.last_name = last_name
	user.save()
	
	if user_type == CustomUser.STAFF:
		Staffs.objects.create(admin=user)
	elif user_type == CustomUser.STUDENT:
		Students.objects.create(admin=user)
	elif user_type == CustomUser.HOD:
		AdminHOD.objects.create(admin=user)
	return render(request, 'login_page.html')

	
def logout_user(request):
	logout(request)
	return HttpResponseRedirect('/')


def get_user_type_from_email(email_id):
	"""
	Returns CustomUser.user_type corresponding to the given email address
	email_id should be in following format:
	'<username>.<staff|student|hod>@<college_domain>'
	eg.: 'abhishek.staff@jecrc.com'
	"""

	try:
		email_id = email_id.split('@')[0]
		email_user_type = email_id.split('.')[1]
		return CustomUser.EMAIL_TO_USER_TYPE_MAP[email_user_type]
	except:
		return None
