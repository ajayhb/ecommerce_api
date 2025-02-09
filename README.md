# E-Commerce RESTful API

A production-ready Django REST framework-based API for managing products and orders.

## 🚀 Features
- View and add products
- Place orders with stock validation
- Exception handling with meaningful error responses
- PEP8-compliant code
- Fully dockerized setup

## 🔧 Installation & Setup

1. **Clone the repository**
   ```sh
   git clone https://github.com/yourusername/ecommerce_api.git
   cd ecommerce_api

2. **Create a virtual environment & install dependencies**
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt


3. **Apply database migrations**
python manage.py migrate

4. **Run the development server**
python manage.py runserver

5. 🐳 **Running with Docker**
docker build -t ecommerce-api .
docker run -p 8000:8000 ecommerce-api

🛠 **API Endpoints**
Method	Endpoint	Description
GET	/products/	- Get all products
POST	/products/	- Add a new product
POST	/orders/	   - Place an order


**✅ Running Tests**
python manage.py test

**📝 License**
This project is open-source.