# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
