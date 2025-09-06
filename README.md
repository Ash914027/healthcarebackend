# Healthcare Application Backend System Assignment

The goal of this assignment is to create a backend system for a healthcare application using Django, Django REST Framework (DRF), and PostgreSQL. The system should allow users to register, log in, and manage patient and doctor records securely.

## Requirements
- Use Django and Django REST Framework (DRF) for the backend.
- Use PostgreSQL as the database.
- Implement JWT authentication for user security using `djangorestframework-simplejwt`.
- Create RESTful API endpoints for managing patients and doctors.
- Use Django ORM for database modeling.
- Implement error handling and validation.
- Use environment variables for sensitive configurations.

## APIs to be Implemented

### 1. Authentication APIs
- **POST** `/api/auth/register/` - Register a new user with name, email, and password.
- **POST** `/api/auth/login/` - Log in a user and return a JWT token.

### 2. Patient Management APIs
- **POST** `/api/patients/` - Add a new patient (Authenticated users only).
- **GET** `/api/patients/` - Retrieve all patients created by the authenticated user.
- **GET** `/api/patients/<id>/` - Get details of a specific patient.
- **PUT** `/api/patients/<id>/` - Update patient details.
- **DELETE** `/api/patients/<id>/` - Delete a patient record.

### 3. Doctor Management APIs
- **POST** `/api/doctors/` - Add a new doctor (Authenticated users only
