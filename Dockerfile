FROM python:3.10-slim
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update && pip install poetry==1.2.1

COPY pyproject.toml poetry.lock ./

RUN poetry install -n --no-root

COPY . /app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]