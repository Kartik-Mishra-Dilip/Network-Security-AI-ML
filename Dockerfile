FROM python:3.10  
# Change to a more complete base image
WORKDIR /app
COPY . /app

# Update and install awscli, adding retries
RUN apt-get update -y && \
    apt-get install -y awscli || exit 0 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "app.py"]