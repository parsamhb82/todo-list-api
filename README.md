# Todo List API

A RESTful Todo List backend built with:

* Django
* Django REST Framework
* PostgreSQL
* Docker

## Features

* Create labels
* Create tasks
* Update labels
* Update tasks
* Delete labels
* Delete tasks
* Drag-and-drop style task ordering
* PostgreSQL database
* Docker support

---

# Clone the Repository

```bash
git clone https://github.com/parsamhb82/todo-list-api.git
cd todo-list-api
```

---

# Running Without Docker

## Prerequisites

* Python 3.13+
* PostgreSQL

## Create Virtual Environment

Linux/macOS:

```bash
python3 -m venv env
source env/bin/activate
```

Windows:

```bash
python -m venv env
env\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Create PostgreSQL Database

Connect to PostgreSQL:

```bash
psql -U postgres
```

Create database and user:

```sql
CREATE DATABASE todo_db;

CREATE USER todo_user WITH PASSWORD 'your_password';

GRANT ALL PRIVILEGES ON DATABASE todo_db TO todo_user;

ALTER SCHEMA public OWNER TO todo_user;
```

## Create Environment File

Create a file named:

```text
.env
```

Example:

```env
DEBUG=True
SECRET_KEY=change_me
DB_PASSWORD=your_password
```

## Apply Migrations

```bash
python manage.py migrate
```

## Run Server

```bash
python manage.py runserver
```

Server will be available at:

```text
http://127.0.0.1:8000
```

---

# Running With Docker

## Prerequisites

* Docker
* Docker Compose

## Create Environment File

Create:

```text
.env
```

Example:

```env
DEBUG=True
SECRET_KEY=change_me
DB_PASSWORD=your_password
```

## Build and Start Containers

```bash
docker compose up --build
```

## Run Migrations

If migrations are not executed automatically:

```bash
docker compose exec web python manage.py migrate
```

## Access Application

```text
http://127.0.0.1:8000
```

---

# Project Structure

```text
todo_list/
├── task/
├── todo_list/
├── manage.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env.example
└── README.md
```

---

# API Endpoints

## Create Label

### Request

```http
POST /task/create-label/
```

### Body

```json
{
  "name": "Work"
}
```

### Example

```bash
curl -X POST http://127.0.0.1:8000/task/create-label/ \
-H "Content-Type: application/json" \
-d '{"name":"Work"}'
```

---

## Create Task

### Request

```http
POST /task/create-task/
```

### Body

```json
{
  "name": "Finish Assignment",
  "label": 1
}
```

### Example

```bash
curl -X POST http://127.0.0.1:8000/task/create-task/ \
-H "Content-Type: application/json" \
-d '{"name":"Finish Assignment","label":1}'
```

---

## Get All Labels With Tasks

Tasks are ordered by:

1. Unfinished tasks first
2. Sort value ascending

### Request

```http
GET /task/labels/
```

### Example

```bash
curl http://127.0.0.1:8000/task/labels/
```

### Response

```json
[
  {
    "id": 1,
    "name": "Work",
    "tasks": [
      {
        "id": 1,
        "name": "Finish Assignment",
        "is_finished": false,
        "sort": 1.0,
        "dead_line": null
      }
    ]
  }
]
```

---

## Update Label

### Request

```http
PATCH /task/label/<id>/
```

### Body

```json
{
  "name": "University"
}
```

### Example

```bash
curl -X PATCH http://127.0.0.1:8000/task/label/1/ \
-H "Content-Type: application/json" \
-d '{"name":"University"}'
```

---

## Update Task

### Request

```http
PATCH /task/task/<id>/
```

### Body

```json
{
  "name": "Study Operating Systems",
  "is_finished": true,
  "dead_line": "2026-06-20T10:00:00Z"
}
```

### Example

```bash
curl -X PATCH http://127.0.0.1:8000/task/task/1/ \
-H "Content-Type: application/json" \
-d '{"is_finished":true}'
```

---

## Move Task

Moves a task between two neighboring tasks.

### Request

```http
POST /task/task/<id>/move/
```

### Body

```json
{
  "previous_task_id": 5,
  "next_task_id": 6
}
```

The new sort value is calculated as:

```text
(previous.sort + next.sort) / 2
```

### Example

```bash
curl -X POST http://127.0.0.1:8000/task/task/3/move/ \
-H "Content-Type: application/json" \
-d '{
  "previous_task_id": 5,
  "next_task_id": 6
}'
```

---

## Delete Task

### Request

```http
DELETE /task/task/<id>/delete/
```

### Example

```bash
curl -X DELETE \
http://127.0.0.1:8000/task/task/1/delete/
```

---

## Delete Label

Deleting a label automatically deletes all tasks that belong to it.

### Request

```http
DELETE /task/label/<id>/delete/
```

### Example

```bash
curl -X DELETE \
http://127.0.0.1:8000/task/label/1/delete/
```

---

# License

This project is intended for an interview
