# Data Model

## 1. User
- `id`: UUID (Primary Key)
- `username`: String (elkin009)
- `created_at`: DateTime

## 2. AuditSession
- `id`: UUID (Primary Key)
- `user_id`: Foreign Key (Link to User)
- `file_type`: Enum (PYTHON, SQL)
- `raw_content`: Text (The code uploaded)
- `timestamp`: DateTime

## 3. AuditFinding
- `id`: UUID (Primary Key)
- `session_id`: Foreign Key (Link to AuditSession)
- `severity`: Enum (CRITICAL, HIGH, MEDIUM, LOW)
- `description`: Text (What is wrong?)
- `suggestion`: Text (How to fix?)
- `line_number`: Integer
