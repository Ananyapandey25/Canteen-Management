# 🍔 Canteen Management System

> **A simple, modern, and beginner-friendly college canteen management system built with Python & Flask.**

## 🌟 About The Project

**Canteen Management System** is a web-based college canteen application designed to make food ordering and basic canteen management simple and convenient.

The project provides a clean interface where students can explore available food items and place orders, while an administrator can access a dedicated dashboard through a **demo login session** to manage the canteen.

The project is intentionally designed with a simple architecture so that it is easy for beginners and first-year students to understand, modify, and extend.

---

## ✨ Features

### 👨‍🎓 Student Side

* 🏠 Simple and attractive home page
* 🍔 Browse available food items
* 📂 View food categories
* 🛒 Add food items to cart
* 🔢 Manage item quantities
* 💰 Automatic total calculation
* 📦 Place orders
* 📋 View order information

### 👨‍💼 Admin Side

* 🔐 Admin login page
* 🎫 Demo session-based authentication
* 📊 Admin dashboard
* 🍕 View food items
* ➕ Add new food items
* 🗑️ Remove food items
* 📦 View customer orders
* 🔄 Update order status

---

## 🔐 Demo Admin Login

This project currently uses a **demo login/session system** for learning purposes.

```text
Username: admin
Password: admin123
```

> ⚠️ These credentials are for demonstration only and should not be used in a real production application.

---

## 🛠️ Tech Stack

| Technology       | Purpose                       |
| ---------------- | ----------------------------- |
| 🐍 Python        | Core programming language     |
| 🌶️ Flask        | Web application framework     |
| 🌐 HTML5         | Page structure                |
| 🎨 CSS3          | User interface & styling      |
| 🔐 Flask Session | Demo login/session management |

---

## 📁 Project Structure

```text
Canteen-Management/
│
├── app.py
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── menu.html
│   ├── cart.html
│   ├── orders.html
│   └── admin.html
│
├── static/
│   └── style.css
│
├── requirements.txt
│
└── README.md
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Ananyapandey25/Canteen-Management.git
```

### 2️⃣ Move Into The Project

```bash
cd Canteen-Management
```

### 3️⃣ Create a Virtual Environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

Linux / macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Run The Application

```bash
python app.py
```

### 6️⃣ Open In Browser

```text
http://127.0.0.1:5000
```

---

## 🔄 Application Flow

```text
                 🍔 CANTEEN MANAGEMENT
                          │
                          ▼
                    🏠 HOME PAGE
                          │
              ┌───────────┴───────────┐
              ▼                       ▼
         👨‍🎓 STUDENT              👨‍💼 ADMIN
              │                       │
              ▼                       ▼
          🍕 MENU                 🔐 LOGIN
              │                       │
              ▼                       ▼
           🛒 CART              📊 DASHBOARD
              │                       │
              ▼                ┌──────┴──────┐
        📦 PLACE ORDER          ▼             ▼
              │             🍔 MENU        📦 ORDERS
              ▼                │             │
        📋 ORDER STATUS        ▼             ▼
                         ➕ / 🗑️ ITEMS   🔄 STATUS
```

---

## 🎯 Project Objectives

The main objectives of this project are:

* Learn the fundamentals of **Python web development**
* Understand how **Flask routing** works
* Build webpages using **HTML and CSS**
* Understand **GET and POST requests**
* Implement basic **session-based login**
* Practice form handling
* Understand basic CRUD operations
* Build a real-world inspired college application

---

## 🔮 Future Improvements

The current version is intentionally simple. Future versions can include:

* 🗄️ MySQL / SQLite database
* 👤 Student registration and login
* 🔒 Secure password hashing
* 💳 Online payment integration
* 📱 Fully responsive mobile UI
* 🔔 Real-time order notifications
* 📊 Admin analytics dashboard
* 🧾 Digital bills and receipts
* ⭐ Food ratings and reviews
* 📧 Email order confirmation
* 🔑 Production-ready authentication

---

## 📸 Screenshots

Screenshots can be added here as the project UI evolves.

```text
screenshots/
├── home.png
├── login.png
├── menu.png
├── cart.png
└── admin-dashboard.png
```

---

## 🧑‍💻 Developer

### **Ananya Pandey**

🎓 Student Developer
🐍 Python & Flask
🌐 Web Development
🍔 Canteen Management System

---

## 📚 Learning Project

This project was created as an educational project to practice **Python, Flask, web development, routing, forms, and session management**.

It is designed to demonstrate how a simple real-world application can be developed using beginner-friendly technologies.

---

## ⭐ Support

If you found this project useful or interesting, consider giving the repository a ⭐ on GitHub!

---

### 🍔 Made with Python & Flask

**Built for learning. Designed for simplicity. Created by Ananya Pandey.**
