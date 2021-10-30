FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

RUN pip install --no-cache-dir \
	Pillow \
	torch \
	transformers \
	requests \
	joblib \
	sklearn \
	python-multipart

COPY ./app/ /app/app/

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
