# E-Commerce RESTful API

A production-ready Django REST framework-based API for managing products and orders.

## 🚀 Features
- View and add products
- Place orders with stock validation
- Exception handling with meaningful error responses
- PEP8-compliant code
- Fully dockerized setup (no local installation needed!)

## 🐳 Running with Docker
> **No need to install Django or dependencies manually! Everything runs inside Docker.**

1. **Clone the repository**
   ```sh
   git clone https://github.com/yourusername/ecommerce_api.git
   cd ecommerce_api
   ```

2. 🐳 **Running the Docke commandsr**
```
docker build -t ecommerce-api .
docker run -p 8000:8000 ecommerce-api
```

🛠 **API Endpoints**
- Method    Endpoint          Description
- GET       /products/        Get all products
- POST      /products/        Add a new product
- POST      /orders/          Place an order


**✅ Running Tests**
```
docker run ecommerce-api python manage.py test
```

**📝 License**
- This project is open-source.

🔹 Final Thoughts
✔ No manual setup required for reviewers

✔ Runs entirely inside Docker (DB migrations + API)

✔ Easy testing with docker run ecommerce-api python manage.py test
