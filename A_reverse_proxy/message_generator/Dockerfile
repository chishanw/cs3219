FROM python:3.7-alpine

WORKDIR /app

COPY version.txt .

RUN pip install -r version.txt

COPY . .

EXPOSE 5002

CMD ["python", "message_generator.py"]
