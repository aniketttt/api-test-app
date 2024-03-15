FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN apt install python3-pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app/routes.py"]
