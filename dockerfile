# Use the official Python image as the base image
FROM python:3.10-slim-buster

# Set the working directory within the container
WORKDIR /app

# Copy over our requirements file
COPY requirements.txt requirements.txt

# Install dependencies using pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy code into the container
COPY . .

# Start FastAPI app using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
