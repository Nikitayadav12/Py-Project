# Flask User Management REST API

## 📌 Objective
Create a REST API that manages user data using Python and Flask.

---

## 🛠 Tools & Technologies
- **Python**
- **Flask**
- **Postman** or **curl** for testing

---

## 🚀 Features
- **GET** all users
- **GET** single user by ID
- **POST** create a new user
- **PUT** update existing user
- **DELETE** remove user
- **In-memory storage** using a Python dictionary

---

## 📂 Project Structure
-flaskapp.py

access:http://127.0.0.1:5000

## API Documentation
View the live Postman documentation here: [User Management API Docs]()
GET All user:http://127.0.0.1:5000/users
GET Single user:http://127.0.0.1:5000/users/1
POST create user:http://127.0.0.1:5000/users
Body:{
    "name": "Alice",
    "email": "alice@example.com"
}

PUT Update user:http://127.0.0.1:5000/users/1
DELETE User:http://127.0.0.1:5000/users/1

##  This is Final!
