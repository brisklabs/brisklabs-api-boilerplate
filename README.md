# 🚀 Brisklabs API Boilerplate

A clean and modular FastAPI boilerplate built with Python — designed for rapid backend development at **Brisklabs**.

---

## 📦 Features

- 🔐 Auth endpoints (register, login, forgot password)
- 📄 Uniform response structure with status codes
- 🧪 Swagger and ReDoc documentation out of the box
- 🧱 Modular route structure (`/auth`, `/user`, etc.)
- ⚙️ Ready for extension with JWT, databases, and more

---

## 🛠️ Getting Started

### 1. Clone the repository

```bash
> git clone https://github.com/your-username/brisklabs-api-boilerplate.git
> cd brisklabs-api-boilerplate
> python3 -m venv venv
> source venv/bin/activate
> pip install -r requirements.txt
> uvicorn app.main:app --reload

```

## 📚 API Documentation
Once the server is running, you can explore the API docs:
🧪 Swagger UI – http://127.0.0.1:8000/docs
📘 ReDoc – http://127.0.0.1:8000/redoc
📂 OpenAPI JSON – http://127.0.0.1:8000/openapi.json

---

## 📁 Project Structure
```
app/
│
├── main.py                # FastAPI app instance
├── models/                # Pydantic models (schemas)
├── routes/                # Route modules (auth, user, etc.)
│   ├── auth.py
│   └── user.py
├── core/                  # Configs, utilities, helpers
└── ...

```

## ✅ Next Steps
- 🔐 Add JWT-based auth
- 🗃️ Connect to a database (PostgreSQL, MongoDB, etc.)
- 🧪 Write unit tests
- 🚀 Prepare Docker deployment

---

## 👨‍💻 Maintained by Brisklabs