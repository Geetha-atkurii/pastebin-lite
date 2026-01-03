# Pastebin-Lite Backend (FastAPI)

A lightweight Pastebin-like backend built with FastAPI.  
Users can create text pastes, share links, and retrieve pastes with optional
time-based expiry (TTL) and view-count limits.

This project is designed to pass automated backend tests and demonstrate
clean backend architecture.

---

## Features

- Create a paste with arbitrary text
- Shareable URL for viewing a paste
- Fetch paste via API (JSON)
- View paste via browser (HTML)
- Optional TTL (time-to-live) expiry
- Optional max view count
- Deterministic time support for testing
- Persistent storage (SQLite)

---

## Tech Stack

- FastAPI
- SQLAlchemy (async)
- SQLite (file-backed persistence)
- Pydantic
- Uvicorn

---

## Project Structure

app/
├── main.py # App entry point
├── config.py # Environment configuration
├── database.py # DB engine & session
├── models.py # SQLAlchemy models
├── routes/ # API & HTML routes
├── services/ # Business logic
├── dao/ # Database access
├── schemas/ # Request/response schemas
└── utils/ # Helpers (time, etc.)

# Create virtual environment
python -m venv venv

# Activate venv
# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn app.main:app --reload

# The server will start at
http://127.0.0.1:8000

# Swagger API docs:
http://127.0.0.1:8000/docs

# Persistence Layer
SQLite (file-backed database)
Managed using SQLAlchemy (async engine)
Database file is automatically created on startup
Suitable for serverless and small-scale deployments

# API Endpoints:
HealthCheck -> GET /api/healthz
Create Paste -> POST /api/pastes
Fetch Paste -> GET /api/pastes/{paste_id}
View Paste -> GET /p/{paste_id}

# Deterministic Time Support (Testing)
When TEST_MODE=1 is enabled, the application uses the request header:
x-test-now-ms: <milliseconds since epoch>

as the current time for expiry logic only.
This is required for deterministic automated testing.