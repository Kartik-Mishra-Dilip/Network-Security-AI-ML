FROM python:3.10-slim-buster
WORKDIR /app
COPY . /app

# Update and install awscli, and clean up
RUN apt-get update -y && \
    apt-get install -y awscli && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "app.py"]