# more_tech_vtb

    python -m venv venv
---
    pip install poetry
---
    poetry install
---
    uvicorn main:app старт апишки
---
    127.0.0.1:8000/docs - дока в Swagger
---
Деплой на сервере: git clone ...
---
    docker-compose -f docker-compose-ci.yaml up -d
    зайти внутрь контейнера docker -t -i <container_name> bash
    cd alembic; mkdir versions
    alembic revision --autogenerate
    alembic upgrade head
  

