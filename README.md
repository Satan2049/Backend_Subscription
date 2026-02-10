# Subscription Backend API

A simple and clean backend project built with **FastAPI** and **PostgreSQL**.
This project is designed as a portfolio sample to demonstrate backend fundamentals,
clean architecture, and real-world API development practices.

---

## 🚀 Features

- FastAPI-based REST API
- PostgreSQL database
- SQLAlchemy ORM
- Modular project structure
- Environment-based configuration
- Automatic database table creation
- Health check endpoint
- User CRUD foundation

---

## 🛠 Tech Stack

- **Python 3.10+**
- **FastAPI**
- **PostgreSQL**
- **SQLAlchemy**
- **Pydantic**
- **Uvicorn**

---

## 📂 Project Structure

```text
app/
├── api/
│ └── v1/
│ └── users.py
├── core/
│ └── config.py
├── db/
│ ├── base.py
│ ├── init_db.py
│ └── session.py
├── models/
│ └── user.py
├── schemas/
│ └── user.py
└── main.py
```

---

## ⚙️ Setup & Run

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd backend-subscription
```

### 2. Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # Linux / Mac
.venv\Scripts\activate     # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment variables

Create a ```text .env``` file in the project root and put this code in it:

```bash
DATABASE_URL=postgresql://postgres:password@localhost:5432/subscription_db
```

### 5. Run the server
```bash
uvicorn app.main:app --reload
```

---

## 🔎 API Docs

Once the server is running, open:

Swagger UI:
http://127.0.0.1:8000/docs

Health Check:
```http request
GET /health
```

### 🧪 Example Response
```json
{
  "status": "ok"
}
```

### 📌 Notes

- This project is intended as a learning and portfolio project
- Authentication and advanced features can be added in future versions

### توضیح فارسی 

این پروژه یک نمونه‌کار بک‌اند است که با FastAPI و PostgreSQL پیاده‌سازی شده
و هدف آن نمایش ساختار استاندارد بک‌اند، کار با دیتابیس، ORM و طراحی API است.
