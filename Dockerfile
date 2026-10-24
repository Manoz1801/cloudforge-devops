FROM python:3.12-slim

WORKDIR /app

COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

RUN useradd --no-create-home --uid 10001 appuser
USER 10001

EXPOSE 5000

CMD ["python", "app.py"]
