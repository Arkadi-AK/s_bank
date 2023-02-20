# The best bank on FastApi

## Launching the project
- ```mv .env.example .env```
- ```docker compose up -d --build```
---
- ```uvicorn main:app --reload```

## Migrations
- ```alembic init migrations```
- ```alembic revision --autogenerate -m "Message"``` создание миграций
- ```alembic upgrade head``` применение миграций

---

## Endpoints

- ```http://127.0.0.1:8000/docs```
