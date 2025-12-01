# 🖥️ Network Availability Monitoring (Flask + SQLite)

Web Application **Monitoring Availability Network** features:
- ✅ Login (SHA256 hashing)
- ✅ Dashboard machine status with AJAX (Connect, Reconnecting, Disconnect)
- ✅ CRUD User
- ✅ CRUD Machine
- ✅ Real-time status update via **ping**
- ✅ Auto-refresh dashboard **AJAX**
- ✅ API endpoint for JSON data

---

## 📂 **Folder Structure**
```
project/
│── app.py                # Main Flask app 
│── auto_update.py        # Optional: status update background
│── network_monitor.db    # Database SQLite
│── templates/            # HTML templates
│    ├── login.html
│    ├── dashboard.html
│    ├── users.html
│    └── machines.html
│── static/
│    └── style.css        # Custom CSS
```

---

## ⚙️ **Instalasi**
1. Clone repository:
   ```bash
git clone https://github.com/username/network-monitoring.git
cd network-monitoring
```
2. Make virtual environment (optional):
   ```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```
3. Install dependencies:
   ```bash
pip -r requirements.txt
```

---

username and password default `network_monitor.db`:
```
Username: ctr
Password: 123
```

---

## 🚀 **Running the Application**
```bash
python app.py
```
Access via browser:
```
http://127.0.0.1:5000/login
```

---

## 🔄 **Auto-refresh Dashboard**
-Dashboard will automated refresh in 5 secound via AJAX.
- API endpoint:
```
GET /api/machines
```
Example Output:
```json
[
    {"id": 1, "name": "Server1", "ip_address": "192.168.1.10", "status": "Connect"},
    {"id": 2, "name": "Server2", "ip_address": "192.168.1.11", "status": "Disconnect"}
]
```

---

## 🛠️ **Optional: Update Status in Background**
Run:
```bash
python auto_update.py
```
This is re-new status machine in 10 second with out waiting for request. 

---

## 🌐 **Deploy ke GitHub**
1. Make a repository in GitHub.
2. Push project:
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
1. Login to [Render](https://render.com).
2. Make **New Web Service**.
3. Connect to repo GitHub.
4. **Build Command**:
   ```bash
pip install -r requirements.txt
```
5. **Start Command**:
   ```bash
gunicorn app:app
```
6. Add file `requirements.txt`:
   ```
flask
gunicorn
```

---
