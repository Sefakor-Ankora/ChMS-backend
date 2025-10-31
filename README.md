# 🛐 Church Management System (ChMS) — Backend API

## 📖 Overview
The **Church Management System (ChMS)** is a web-based platform for managing church operations, including members, attendance, donations, communications, and events.  
This repository contains the **Django REST Framework (DRF)** backend API.

---

## 🧱 Tech Stack
- **Backend Framework:** Django 5 + Django REST Framework  
- **Auth:** JWT (via `djangorestframework-simplejwt`)  
- **Docs:** Swagger + ReDoc (via `drf-yasg`)  
- **Database:** SQLite (development), PostgreSQL (production ready)  
- **CORS:** Enabled for frontend integration (React app)

---


## 🚀 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/chms-backend.git
cd chms-backend
````

### 2️⃣ Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

### 6️⃣ Run Server

```bash
python manage.py runserver
```

---

## 🧩 API Documentation

| Type           | URL                                                              |
| -------------- | ---------------------------------------------------------------- |
| **Swagger UI** | [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/) |
| **ReDoc UI**   | [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)     |

---

## 🔐 Authentication

The system uses **JWT Authentication**.

### Obtain Token

`POST /api/token/`

```json
{
  "username": "admin",
  "password": "yourpassword"
}
```

### Refresh Token

`POST /api/token/refresh/`

```json
{
  "refresh": "<your_refresh_token>"
}
```

Use the access token in the `Authorization` header:

```
Authorization: Bearer <access_token>
```

---

## 📂 API Endpoints Overview

| Feature | Method | Endpoint              | Description             |
| ------- | ------ | --------------------- | ----------------------- |
| Members | `GET`  | `/api/members/`       | List all members        |
| Members | `POST` | `/api/members/`       | Create new member       |
| Members | `GET`  | `/api/members/{id}/`  | Retrieve member details |
| Auth    | `POST` | `/api/token/`         | Obtain JWT tokens       |
| Auth    | `POST` | `/api/token/refresh/` | Refresh access token    |

---

## 🧠 Developer Notes

* Ensure your React frontend runs on `http://localhost:3000`
* Update `CORS_ALLOWED_ORIGINS` in `settings.py` for production
* Use `.env` file to store sensitive credentials (e.g., DB, secret key)

---

## 🧾 License

MIT License © 2025 Sefakor(https://github.com/Sefakor-Ankora)


---

## 📘 API Endpoints Overview

Below is the complete list of active API endpoints for the **Church Management System (ChMS)** backend.

---

### 🔐 Authentication

| Feature | Method | Endpoint | Description |
|----------|---------|----------|--------------|
| Login | `POST` | `/api/token/` | Obtain JWT access and refresh tokens |
| Refresh Token | `POST` | `/api/token/refresh/` | Refresh access token |
| Register | `POST` | `/api/register/` | Create new user and member profile |

---

### 👥 Members

| Method | Endpoint | Description |
|---------|-----------|-------------|
| `GET` | `/api/members/` | Retrieve all member profiles |
| `POST` | `/api/members/` | Add a new member |
| `GET` | `/api/members/{id}/` | Retrieve single member details |
| `PUT` | `/api/members/{id}/` | Update a member record |
| `DELETE` | `/api/members/{id}/` | Delete a member record |

---

### 🗓️ Attendance

| Method | Endpoint | Description |
|---------|-----------|-------------|
| `GET` | `/api/attendance/` | List all attendance records |
| `POST` | `/api/attendance/` | Record a member's attendance |
| `GET` | `/api/attendance/{id}/` | Retrieve a single attendance record |
| `PUT` | `/api/attendance/{id}/` | Update attendance record |
| `DELETE` | `/api/attendance/{id}/` | Delete an attendance record |

**Example Request:**
```json
{
  "member": 1,
  "event_type": "service",
  "present": true,
  "remarks": "Attended main service"
}
