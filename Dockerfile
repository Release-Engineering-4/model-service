FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN pip install poetry
RUN poetry install --no-cache

EXPOSE 5000

CMD ["poetry", "run", "python", "model_service/app.py"]