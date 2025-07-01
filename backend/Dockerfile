FROM python:3.9-slim

# Install SSL certificates and networking tools
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    dnsutils \
    && rm -rf /var/lib/apt/lists/*

# Update CA certificates
RUN update-ca-certificates --fresh

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD ["sh", "-c", "python wait_for_mysql.py && python app.py && gunicorn -w 4 -b :5000 app:app"]