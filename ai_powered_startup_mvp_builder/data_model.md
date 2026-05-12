# Data Model

## 1. User (Local Storage for MVP)
- `id`: UUID
- `username`: String
- `preferences`: JSON Object

## 2. Subject
- `id`: UUID
- `name`: String
- `difficulty_level`: Integer (1-5)
- `exam_date`: DateTime

## 3. StudyTask
- `id`: UUID
- `subject_id`: Foreign Key
- `title`: String
- `duration_minutes`: Integer
- `is_completed`: Boolean
- `scheduled_date`: Date
