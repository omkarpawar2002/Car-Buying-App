# 🚗 Buy Car — Django CRUD Application with Authentication

Buy Car is a Django-based web application that allows users to **buy**, **update**, and **delete** car records. The app also includes **built-in user authentication** for secure access.

---

## 🧰 Features

- ✅ User Registration, Login, Logout (Django's built-in auth)
- ✅ Add a new car
- ✅ View list of available cars
- ✅ Update car details
- ✅ Delete car entries
- ✅ Function-Based Views (FBVs)

---

## 🗂️ Project Structure

```
buy_car/
├── .env/                 # Virtual environment (ignored by Git)
├── buy_car/              # Main Django project folder
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── app_name/             # Your Django app (replace with real name)
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── templates/
├── requirements.txt      # Project dependencies
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

Follow these steps to run the project locally:

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/omkarpawar2002/buy-car.git
cd buy-car
```

---

### 2️⃣ Create Virtual Environment (Optional but Recommended)

```bash
# For Windows:
python -m venv .env
.env\Scripts\activate

# For macOS/Linux:
python3 -m venv .env
source .env/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5️⃣ Create Superuser (Admin Access)

```bash
python manage.py createsuperuser
```

Follow the prompt to set up a username and password.

---

### 6️⃣ Run the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

---

## 🔐 Authentication

This project uses **Django's built-in authentication system** for:
- User Signup
- Login/Logout
- Session Management
- Restricting CRUD access to authenticated users

---

## 🛠️ Technologies Used

- Python
- Django
- HTML/CSS (for templates)
- SQLite (default Django database)
- Bootstrap (optional, if used in templates)

---

## 📦 Requirements

All Python package dependencies are listed in `requirements.txt`.  
You can generate it using:

```bash
pip freeze > requirements.txt
```

---

## 🧾 License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).

---

## 🙋‍♂️ Author

**Omkar Pawar**  
🔗 [GitHub Profile](https://github.com/omkarpawar2002)  
📧 omkarsp20@gmail.com

---

## 💡 Suggestions or Contributions?

Feel free to open an issue or submit a pull request. Contributions are welcome!