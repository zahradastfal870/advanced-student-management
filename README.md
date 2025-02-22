📚 Advanced Student Management System (SMS v2)
🔹 Overview
The Advanced Student Management System (SMS v2) is a Python-based application that allows users to manage student records securely. It includes user authentication, password validation, student CRUD operations, and academic score tracking. The system uses SQLAlchemy as an ORM with an SQLite database.
🚀 Features
✅ Secure User Authentication (Registration & Login)
✅ Password Validation & Security (Special characters, numbers, case rules)
✅ CRUD Operations (Add, View, Update, Delete students)
✅ SQLite Database Integration (Efficient data storage)
✅ Student Score Management (Query and update scores)
✅ Validation Checks (Names, phone numbers, and student data)
🛠 Technologies Used
- Python 🐍
- SQLAlchemy (ORM)
- SQLite (Database)
- Regular Expressions (`re` module)
📂 Project Structure
📦 student-management-system
 ┣ 📜 main.py                # Main application logic
 ┣ 📜 database_setup.py       # Database schema with SQLAlchemy
 ┣ 📜 sms.db                 # SQLite database file

📌 Installation & Setup
1️⃣ Clone the Repository
```sh
git clone https://github.com/zahradastfal870/advanced-student-management.git
cd advanced-student-management
```
2️⃣ Install Dependencies
```sh
pip install sqlalchemy
```
3️⃣ Initialize the Database (Only Once)
```sh
python database_setup.py
```
▶️ How to Run the Application
Run the Main Script
```sh
python main.py
```
After running this command, you will see the **Welcome Menu**. From there, you can:
1. **Login** if you already have an account.
2. **Register** a new account.
3. **Manage Student Records** (Add, Update, Delete, View).
4. **Query Student Scores** by name or ID.
👨‍💻 Contributors
Zahra Dastfal ([GitHub Profile](https://github.com/zahradastfal870))
📜 License
This project is licensed under the MIT License.
