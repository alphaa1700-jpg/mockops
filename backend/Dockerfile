FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y netcat-openbsd curl
RUN pip install fastapi uvicorn sqlalchemy psycopg2-binary
RUN pip install fastapi uvicorn sqlalchemy psycopg2-binary prometheus-fastapi-instrumentator

RUN chmod +x wait-for-db.sh

CMD ["sh", "wait-for-db.sh"]
