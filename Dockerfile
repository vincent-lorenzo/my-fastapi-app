# 1. Use a official Python image as a starting point
FROM python:3.13-slim

# 2. Set the working directory inside the container to /app
WORKDIR /app

# 3. Copy our requirements file into the container
COPY requirements.txt .

# 4. Tell the container to install the libraries on the list
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy all our files (main.py, etc.) into the container
COPY . .

# 6. Tell the container how to start the app when it's turned on
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]