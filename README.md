# Employee Data Generator & Analytics - Django REST API

A Django-based web application that generates synthetic employee data, stores it in a PostgreSQL database, and exposes REST API endpoints for analytical summaries with visualization support.

---

## 🚀 Features

- Generate synthetic employee records (via custom `generate_data` command)
- PostgreSQL database integration
- RESTful APIs with pagination and filtering
- Swagger UI for API exploration
- Basic data visualization (Chart.js / Swagger)
- Environment variable-based configuration (`.env`)
- DRF Authentication and rate-limiting

---

## 🛠 Technologies

- Python 3.10+
- Django 4.x
- Django REST Framework
- PostgreSQL
- Faker (for data generation)
- drf-yasg (Swagger UI)
- django-environ (for `.env` config)

---

## 📁 Project Structure

```
employee_dashboard/
├── core/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   ├── management/
│   │   └── commands/
│   │       └── generate_data.py
├── employee_dashboard/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .env
├── manage.py
├── requirements.txt
├── templates/
└── README.md
```

---

## 📦 Setup Instructions

### 1. Clone the Repository
```bash
git clone git@github.com:vishalmanjrekar/django-fullstack-task.git
cd employee-dashboard
```

### 2. Create Virtual Environment & Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Setup PostgreSQL Database
Ensure PostgreSQL is installed and running.
Create a database named `employee_db` (or as specified in `.env`).

```sql
CREATE DATABASE employee_db;
```

### 4. Configure Environment Variables
Create a `.env` file in the project root:

#### ✅ Sample `.env`
```
DEBUG=True

DB_NAME=employee_db
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
```

### 5. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Generate Synthetic Data
```bash
python manage.py generate_data
```

You can specify the number of employees with `--employees` argument.

### 7. Run Development Server
```bash
python manage.py runserver
```

### 8. Explore APIs with Swagger UI
Visit:
```
http://127.0.0.1:8000/swagger/
```


## 🔐 Authentication (Optional)
You can enable token-based authentication using DRF’s TokenAuth:
```bash
python manage.py drf_create_token <username>
```

Then pass the token in headers:
```http
Authorization: Token your-token-here
```

---

## 📈 Visualization
Basic visualizations can be added via:
- Chart.js frontend
- Swagger UI sample data visualization with markdown

---

---

## 🧠 Design Considerations
See `design_decisions.md` for architecture breakdown, model rationale, and tech decisions.

---