# Use official Python image
FROM python:3.10

# Set working directory
# WORKDIR /app

EXPOSE 8000

# Install dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI application
COPY . .

# Command to run the app using uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
