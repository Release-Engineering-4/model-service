FROM python:3.10-slim
WORKDIR /root/
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src src/
COPY models models/

ENTRYPOINT ["python"]
CMD ["src/app.py"]