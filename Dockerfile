# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt file
COPY requirements.txt /app/

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose the port on which your app will run
EXPOSE 8000

# Start the application (adjust the command according to your app)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
