# RVCE Management System

## Overview

This project is a **University Management System** that provides different functionalities for **Students, Staff, and HODs** based on their login credentials. It was built using **HTML, JavaScript, CSS, Bootstrap, Python, Django**, and **SQLite**. The system is designed with a role-based access mechanism where each user type gets a different landing page with relevant functionalities.

---

## **Phase 1: User Authentication System**

The first phase of the project involved the development of the **Login and Signup** system. Users can sign up and log in using their **institutional email IDs**, which follow the format:

`<username>.<staff/hod/student>@rvce.edu.in`

During signup, users provide details such as:

- Email ID
- Password
- Gender
- Address
- Other relevant information

Upon successful login, users are redirected to their respective dashboards based on their role (Student, Staff, or HOD).

---

## **Phase 2: Role-Based Web Application**

Once users log in, they access different functionalities depending on their role.

### **Student Features**

- **Course Registration**: Students can browse and enroll in courses.
- **Attendance Check**: Students can view their attendance records.
- **Results View**: Students can check their academic results.

### **Staff Features**

- **Manage Students**: Staff can view and update student details.
- **Attendance Management**: Staff can mark and update student attendance.
- **Course Management**: Staff can take up a course to teach.
- **Other functionalities**: Various tools to assist staff in student management.

### **HOD Features**

- Includes all **staff** and **student** functionalities.
- **Special Feature: Bulk Upload of Student Data**
  - The HOD can upload an **Excel file** containing student details.
  - The platform extracts and updates student records in the database automatically.
  - (*This functionality is currently limited to HODs but can be extended to staff in the future.*)

### **LLM Integration for Database Querying**

- Instead of manually searching through the database, users can **query the database** using an **LLM (Large Language Model).**
- Example: If the HOD requires the "list of students," the LLM will directly query the database and fetch the relevant data.
- This feature enhances efficiency by reducing manual searches on the website.
  [follow the link for more information on the implementation](https://github.com/Prithiviraj25/query_database_using_llm)

---

## **Phase 3: Business Impact Analysis**

The final phase involved analyzing the **business impact** of various processes in the system using **Machine Learning**.

### **Parameters Considered:**

1. **Recovery Time Objective (RTO)**
2. **Recovery Point Objective (RPO)**
3. **Business Continuity Index (BCI)**
4. **Work Recovery Time (WRT)**
5. **Maximum Tolerable Downtime (MTD)**
6. **Downtime Cost**
7. **Probability of Failure**
8. **Risk Exposure**

### **Machine Learning Approach**

- We trained a **Naïve Bayes** model and an **LLM** on this data.
- The model predicts the **risk level** of each process added to the database.
- The prediction outputs are:
  - **Catastrophic Risk**
  - **High Risk**
  - **Low Risk**
- **Achieved Accuracy**: **94%**

---

## **Technical Stack**

- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Backend**: Python, Django
- **Database**: SQLite
- **Machine Learning**: Naïve Bayes, LLM for querying and risk assessment

Each user role has a unique dashboard, but all dashboards are built on a common **base template**.

---

## **Running the Project**

To set up and run the project:

1. **Create a Virtual Environment**

   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows use: venv\Scripts\activate
   ```

2. **Install Requirements**

   ```sh
   pip install -r requirements.txt
   ```

3. **Run the Server**

   ```sh
   python manage.py runserver
   ```

4. Open a web browser and go to:

   ```sh
   http://127.0.0.1:8000/
   ```

---
## **Screenshots 
1. Front page
   ![Screenshot 2025-02-14 at 4 22 45 PM](https://github.com/user-attachments/assets/941e8a07-ffe1-4e97-980e-ccbdbdcd8357)
   
2. Login page
   ![Screenshot 2025-02-14 at 4 22 54 PM](https://github.com/user-attachments/assets/016092a2-c95e-4e85-9fa2-de5441006c88)

3. Landing page
   ![Screenshot 2025-02-14 at 10 47 31 AM](https://github.com/user-attachments/assets/3c2bbc5f-878e-4a2f-84f2-d7a831a198f4)

4. Excel and student upload
   ![Screenshot 2025-02-14 at 10 47 09 AM](https://github.com/user-attachments/assets/fe303d46-7c17-40f3-b726-5ba9a15e491a)
   ![Screenshot 2025-02-14 at 11 50 21 AM](https://github.com/user-attachments/assets/d8d501f1-3078-495d-9e30-6dc6b2cae7b1)
   ![Screenshot 2025-02-14 at 10 42 16 AM](https://github.com/user-attachments/assets/67964398-4a50-45f0-9d81-8b789c30a878)

5. More features
   ![WhatsApp Image 2025-02-13 at 17 20 01](https://github.com/user-attachments/assets/0fb92a1a-9883-40bb-863a-676688095a4b)


---
## **Future Enhancements**

- Extending **bulk student upload** functionality to staff.
- Improving LLM-based query processing for advanced database interactions.
- Implementing real-time notifications and alerts.
- Enhancing UI/UX for a smoother user experience.

---

## **Contributors**

- **Sanika Kamath**
- **Mukund Vijay**
- **Prithviraj N**
- **Muktha P**
- **Muskan Agarwal**

---

