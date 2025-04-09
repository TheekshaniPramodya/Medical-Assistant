# 🏥 Medical Assistant Web Application

![Medical-Assistant](https://i.ibb.co/kgqvBJhk/mediass.png)


A **Flask & React-based** medical assistant web application designed to help users manage appointments, store medical records, and provide AI-based health suggestions.

## 🚀 Features
- 🏥 **Appointment Management** – Book, edit, and cancel medical appointments.
- 📋 **Medical Records** – Securely store and access past medical records.
- 🤖 **AI Health Assistant** – Get AI-driven health insights.
- 📊 **User Dashboard** – View health statistics and upcoming appointments.
- 🔐 **Secure Authentication** – User authentication and role-based access.

---

## 📂 Folder Structure

medical-assistant/ │── backend/ # Flask backend │ ├── api/ # API routes │ ├── database/ # Database models & scripts │ ├── static/ # Frontend assets (CSS, JS) │ ├── templates/ # HTML templates │ ├── config.py # Configuration settings │ ├── .env # Environment variables │ ├── requirements.txt # Dependencies │── frontend/ # React frontend │ ├── src/ # Main React source files │ ├── public/ # Static files │ ├── package.json # Node.js dependencies │── .gitignore # Files to ignore in Git │── README.md # Project documentation


---

## 🛠️ Installation & Setup

### 🔹 Backend (Flask)
**Clone the repository**  
   ```sh
   git clone https://github.com/TheekshaniPramodya/medical-assistant.git
   cd medical-assistant/backend


**Create a virtual environment

python3 -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)



**Install dependencies

pip install -r requirements.txt



**Set up environment variables

Create a .env file in the backend/ folder:

FLASK_APP=app.py
FLASK_ENV=development
DATABASE_URL=sqlite:///database/medical_assistant.db



**Run the backend

flask run



**** Frontend (React)

**Navigate to the frontend folder

cd ../frontend


**Install dependencies

npm install


**Run the React app

npm start



🖥️ Usage
Open http://localhost:3000 for the frontend.
Open http://127.0.0.1:5000 for the backend API.
📜 License
MIT License © 2025 

📌 Technologies Used
Backend: Flask, SQLite, Flask-RESTful, JWT Authentication
Frontend: React.js, Tailwind CSS, Axios
Database: SQLite (or PostgreSQL/MySQL)
Deployment: Docker (Optional)

🤝 Contributing
Want to contribute? Feel free to create a pull request! 🚀
