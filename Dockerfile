FROM python:3.11-slim

WORKDIR /app

COPY relay.py /app/relay.py
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000/udp

CMD ["python3", "relay.py"]
