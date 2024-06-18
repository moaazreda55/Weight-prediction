FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY ./requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copy the rest of the application code to the working directory
COPY ./myapp.py /app/myapp.py

# Command to run the app using uvicorn
CMD ["uvicorn", "myapp:app", "--host", "0.0.0.0", "--port", "8000"]
