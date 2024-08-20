FROM python:3.11-alpine

WORKDIR /app

RUN apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev \
    # Outros pacotes que possam ser necessários para compilar bibliotecas Python
    && pip install --upgrade pip

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV UVICORN_CMD="uvicorn main:app --host 0.0.0.0 --port 8000 --reload"

EXPOSE 8000

CMD ["sh", "-c", "$UVICORN_CMD"]
