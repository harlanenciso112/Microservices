FROM python:3.12-slim
WORKDIR /products
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "products.py"]
