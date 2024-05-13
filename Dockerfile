FROM python:3.7.17-slim
WORKDIR /root/
COPY requirements.txt .

RUN python -m pip install --upgrade pip &&\
    pip install -r requirements.txt

COPY src src/
COPY models models/

ENTRYPOINT ["python"]
CMD ["src/app.py"]