# Azayd Payroll Management System

## Project Overview

The **Azayd Payroll Management System** is a full-stack web application built using **Flask (Python)** and **SQLite**. It is designed for payroll management in IT consulting firms, enabling admins and HR staff to manage employee records, salaries, and user accounts efficiently.

The system features **role-based access control** with two roles:

- **Admin:** Full access, can manage users and payroll.
- **HR:** Limited access, can only manage payroll.

This project demonstrates secure authentication using **password hashing**, a responsive frontend with **Bootstrap**, and a fully functional database backend.

---

## Features

### User Authentication

- Login and logout functionality with **hashed passwords** using `Werkzeug`.
- Role-based access:
  - **Admin**: Can register new users and manage payroll.
  - **HR**: Can manage payroll only.

### Payroll Management

- Add employee records with name, position, and salary.
- View all employee payroll records.
- Simple and intuitive web interface.

### Security

- Passwords are securely hashed using `Werkzeug` before storing in the database.
- Session-based authentication to protect restricted routes.
- Admin-only routes restricted via a decorator.

### Frontend

- Clean, responsive design using **Bootstrap 5**.
- Separate templates for login, registration, dashboard, and payroll management.
- CSS styling for a modern UI.

---

## Technologies Used

- **Backend:** Python 3, Flask, SQLite
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Authentication:** Werkzeug (password hashing)
- **Database:** SQLite (`payroll.db`)

---

## Project Structure

```
payroll_project/
│
├── app.py                 # Main Flask application
├── payroll.db             # SQLite database with default Admin
├── requirements.txt       # Python dependencies
│
├── static/
│   └── css/
│       └── style.css      # Custom CSS styles
│
└── templates/
    ├── base.html          # Base template
    ├── login.html         # Login page
    ├── register.html      # Registration page (Admin only)
    ├── dashboard.html     # Dashboard for Admin/HR
    └── payroll.html       # Payroll management page
```

---

## Setup Instructions

### 1. Clone or Download

Download the project ZIP and extract it:

```
unzip payroll_project.zip
cd payroll_project
```

### 2. Install Dependencies

Install Python dependencies using pip:

```
pip install -r requirements.txt
```

### 3. Database

The project comes with a preloaded SQLite database (`payroll.db`) containing a default Admin user:

- **Username:** `admin`
- **Password:** `admin123`
- **Role:** Admin

No manual setup is needed; the app will connect to this database automatically.

### 4. Run the Application

Run the Flask app:

```
python app.py
```

The application will start at:

```
http://127.0.0.1:5000/
```

### 5. Usage

1. Navigate to `/login` to log in.
2. Admin users can register new HR/Admin accounts via `/register`.
3. Both Admin and HR can access the payroll management page to add/view employee records.

---

## Default User Roles

| Username | Password | Role  |
| -------- | -------- | ----- |
| admin    | admin123 | Admin |

> Note: New users can be added through the registration page (Admin only).

---

## Security Notes

- Passwords are stored **hashed**, not in plain text.
- Only Admin users can access the user registration page.
- HR users cannot access user management features.

---

## Future Enhancements

- Add edit/delete functionality for payroll records.
- Implement email notifications for payroll updates.
- Move from SQLite to MySQL/PostgreSQL for production.
- Add unit tests for backend routes.
- Enhance dashboard with analytics and charts.

---

## Screenshots

1. **Login Page**
2. **Admin Dashboard**
3. **Payroll Management**
4. **Register User (Admin Only)**

---

## Authors

- **Poorvika N J** – Full-stack development, UI/UX, Backend & DB design

---

## License

This project is for educational and demonstration purposes.

