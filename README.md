# Online Course Enrollment System (Django REST Framework)

## Overview
This project is a backend API for an Online Learning Platform built using **Django REST Framework**.

It allows:
- Instructors to create and manage courses
- Students to enroll in courses
- Each course to have multiple learning modules
- Secure access using JWT Authentication
- API documentation using Swagger (drf-spectacular)
- Performance profiling using Django Silk

---

## Tech Stack
- Python
- Django
- Django REST Framework
- JWT Authentication (SimpleJWT)
- drf-spectacular (Swagger Docs)
- Django Silk (Performance Profiling)

---

## Models Implemented

### User (Custom User Model)
- Email-based authentication
- Roles: `INSTRUCTOR`, `STUDENT`

### Course
- Created by instructor
- Contains multiple modules

### Module
- Belongs to a course
- Duration-based learning unit

### Enrollment
- Student enrolls in multiple courses
- Status: ACTIVE / COMPLETED

---

## Authentication
- JWT based authentication
- Access & Refresh tokens
- Protected endpoints require Bearer Token

---

## API Endpoints

### Auth
- `POST /api/token/`
- `POST /api/token/refresh/`

### Courses
- `GET /api/courses/`
- `GET /api/courses/{id}/`
- `PUT / PATCH / DELETE /api/courses/{id}/`

### Enrollment
- `POST /api/enroll/`
- `GET /api/enrollments/`
- Filter: `?status=ACTIVE`

### Modules
- `GET /api/modules/`
- `POST /api/modules/`

---

## API Documentation
Swagger UI available at: http://127.0.0.1:8000/api/schema/swagger-ui/

## Performance Profiling
Django Silk enabled at: http://127.0.0.1:8000/silk/
Used to analyze:
- Request time
- DB queries
- API performance optimization

---

## Features Achieved
- Custom User Model
- Role-based Permissions
- Nested Serializers
- Filtering & Pagination
- JWT Security
- Swagger Documentation
- Silk Profiling  






