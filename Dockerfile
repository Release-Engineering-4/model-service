FROM python:3.10-slim

WORKDIR /app
COPY . /app

LABEL org.opencontainers.image.source https://github.com/Release-Engineering-4/model-service

RUN pip install poetry
RUN poetry install


EXPOSE 5000

CMD ["poetry", "run", "python", "model_service/app.py"]
