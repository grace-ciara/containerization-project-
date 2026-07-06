# clean, official Python environment
FROM python:3.11-slim

# default working folder inside the container
WORKDIR /app

# copy requirements list 
COPY requirements.txt .

# install all necessary packages 
RUN pip install --no-cache-dir -r requirements.txt

# copy all the project files and subfolders into the container
COPY . .

# tell Docker to automatically execute the main script
CMD ["python", "main.py"]
