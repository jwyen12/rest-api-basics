# Flask Video API

A simple REST API built with Flask and SQLAlchemy that allows users to create, read, update, and delete video records.

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/flask-video-api.git
cd flask-video-api
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Database Setup

Create the database by running:

```bash
python create_db.py
```

This will generate the SQLite database file locally.

---

## Run the Application

```bash
python api.py
```

The API will start in development mode.

---

## Example Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | /videos/<id> | Get a specific video |
| POST   | /videos/<id>  | Create a new video |
| PATCH    | /videos/<id> | Update a video |
| DELETE | /videos/<id> | Delete a video |

---

## Future Improvements

- Add input validation
- Add authentication
- Deploy to a cloud provider
- Switch from SQLite to PostgreSQL
- Add unit tests
