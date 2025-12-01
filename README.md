# 🖥️ Network Availability Monitoring (Flask + SQLite)

A simple web application for **network availability monitoring** with the following features:
- ✅ Login with SHA256 password hashing
- ✅ Dashboard showing machine status (Connect, Reconnecting, Disconnect)
- ✅ CRUD for Users
- ✅ CRUD for Machines
- ✅ Real-time status update using **ping**
- ✅ Auto-refresh dashboard using **AJAX**
- ✅ API endpoint for JSON data

---

## 📂 **Folder Structure**
```
project/
│── app.py                # Main Flask application
│── db-first.py           # Initialize database
│── auto_update.py        # Optional: background status updater
│── network_monitor.db    # SQLite database
│── templates/            # HTML templates
│    ├── login.html
│    ├── dashboard.html
│    ├── users.html
│    └── machines.html
│── static/
│    └── style.css        # Custom CSS
```

---

## ⚙️ **Installation**
1. Clone the repository:
   ```bash
git clone https://github.com/username/network-monitoring.git
cd network-monitoring
```
```

2. Create a virtual environment (optional):
   ```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```
3. Install dependencies:
   ```bash
pip install flask
```

---

## 🗄️ **Initialize Database**
Run:
```bash
python db-first.py
```
This will create `network_monitor.db` and a default user:
```
Username: ctr
Password: 123
```

---

## 🚀 **Run the Application**
```bash
python app.py
```
Access in your browser:
```
http://127.0.0.1:5000/login
```

---

## 🔄 **Auto-refresh Dashboard**
- The dashboard automatically updates every 5 seconds via AJAX.
- API endpoint:
```
GET /api/machines
```
Sample output:
```json
[
    {"id": 1, "name": "Server1", "ip_address": "192.168.1.10", "status": "Connect"},
    {"id": 2, "name": "Server2", "ip_address": "192.168.1.11", "status": "Disconnect"}
]
```

---

## 🛠️ **Optional: Background Status Update**
Run:
```bash
python auto_update.py
```
This updates machine status every 10 seconds without waiting for requests.

---

## 🌐 **Deploy to GitHub**
1. Create a repository on GitHub.
2. Push the project:
   ```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/username/network-monitoring.git
git push -u origin main
```

---

## ☁️ **Deploy to Render (Free)**
1. Log in to [Render](https://render.com).
2. Create a **New Web Service**.
3. Connect to your GitHub repo.
4. **Build Command**:
   ```bash
pip install -r requirements.txt
```
5. **Start Command**:
   ```bash
gunicorn app:app
```
6. Add a `requirements.txt` file:
   ```
flask
gunicorn

ANJENGGGG
```

---
