FROM python:3.9  # Replace with your desired Python version

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "myapp.py"]
