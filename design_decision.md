# Design Decisions

## 🧱 Database Models & Relationships
The application is built around four primary models that reflect a typical employee management system. These models are:

### 1. `Department`
- **Fields**: `name`, `location`
- **Purpose**: Represents company departments. Employees are assigned to one department.

### 2. `Employee`
- **Fields**: `name`, `email`, `department`, `join_date`, `designation`, `salary`
- **Relationships**: ForeignKey to `Department`
- **Purpose**: Stores core employee data. Email is unique to avoid duplication.

### 3. `Attendance`
- **Fields**: `employee`, `date`, `status`
- **Relationships**: ForeignKey to `Employee`
- **Purpose**: Records daily attendance of employees. Useful for calculating absenteeism or presence trends.

### 4. `Performance`
- **Fields**: `employee`, `review_date`, `rating`, `comments`
- **Relationships**: ForeignKey to `Employee`
- **Purpose**: Tracks periodic performance reviews of each employee.

All relationships are normalized using `ForeignKey` to ensure referential integrity and to enable easy filtering, aggregation, and visualization.

---

## ⚙️ Application Architecture

The project is structured into logical Django components:

```
employee_dashboard/
├── core/
│   ├── models.py               # Database schema
│   ├── serializers.py          # DRF serializers
│   ├── views.py                # DRF views (ViewSets)
│   ├── urls.py                 # App-level routes
│   ├── management/
│   │   └── commands/
│   │       └── generate_data.py  # Script to populate test data
│   └── admin.py                # Admin configurations
├── employee_dashboard/
│   ├── settings.py             # Project settings
│   ├── urls.py                 # Project routes
├── .env                        # Environment configuration
├── manage.py
├── templates/
```

---

## 🧪 Data Generation Strategy

A custom Django management command (`generate_data.py`) uses the `Faker` library to populate the database with:

- Departments (e.g., HR, Sales, Engineering)
- Employees with random join dates, salary, and department assignments
- Attendance entries over multiple days
- Performance reviews with random comments and ratings

This ensures enough synthetic data for REST API testing and visualization.

---

## 🧩 API Design Decisions

- **Framework**: Django REST Framework (DRF)
- **Authentication**: DRF TokenAuth (optional, simple integration)
- **Pagination**: LimitOffsetPagination to avoid memory overhead
- **Filtering**: Provided on key fields using `django-filter`
- **Throttling**: DRF’s built-in throttling can be enabled for production readiness
- **Swagger**: `drf-yasg` for interactive docs

## 📦 Environment Configuration

The `.env` file is used for secret and environment-dependent variables:

```
DEBUG=True

DB_NAME=employee_db
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
```

`django-environ` handles the integration in `settings.py`.

---

## 🎯 Design Goals & Justification

- **Simplicity First**: Chose minimal viable models and views to meet challenge goals within 3 hours.
- **Scalable Design**: Easy to extend with projects, payroll, or user roles.
- **Decoupled Layers**: Views, serializers, models are split cleanly for maintainability.
- **No Docker**: Not included to stay within scope and time constraints.

---

## 📌 Summary
This design supports generating, storing, and analyzing employee-related data using Django and DRF. It’s modular, extensible, and fully functional with a PostgreSQL backend.