FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD exec uvicorn core_erp_engine:app --host 0.0.0.0 --port ${PORT}

