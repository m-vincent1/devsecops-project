FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 8080
ENV BACKEND_URL=http://app2-backend:5000
CMD ["python", "app.py"]
