FROM python:3.10

WORKDIR /app



COPY . /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt



CMD ["gunicorn", "-b", "0.0.0.0:5000", "-w", "2", "-k", "uvicorn.workers.UvicornWorker", "--log-level", "info", "main:app"]