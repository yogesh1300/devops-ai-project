# Use Python as base
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements file first
COPY requirements.txt .

# Install all libraries
RUN pip install -r requirements.txt

# Copy all app files
COPY . .

# Tell Docker which port app runs on
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]