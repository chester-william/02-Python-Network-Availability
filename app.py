
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import sqlite3
import hashlib
import random
import subprocess

app = Flask(__name__)
app.secret_key = 'supersecretkey'
DB_NAME = 'network_monitor.db'

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def check_ping(ip):
    try:
        result = subprocess.run(['ping', '-n', '1', ip], capture_output=True, text=True)
        output = result.stdout
        if "TTL" in output:
            return "Connect"
        elif "Destination host unreachable" in output:
            return "Reconnecting"
        elif "Request timed out" in output:
            return "Disconnect"
        else:
            return "Disconnect"
    except Exception:
        return "Disconnect"

def update_machine_status():
    conn = get_db_connection()
    machines = conn.execute('SELECT * FROM machines').fetchall()
    for m in machines:
        status = check_ping(m['ip_address'])
        conn.execute('UPDATE machines SET status = ? WHERE id = ?', (status, m['id']))
    conn.commit()
    conn.close()

@app.route('/')
def index():
    if 'user' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = hashlib.sha256(request.form['password'].encode()).hexdigest()
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
        conn.close()
        if user:
            session['user'] = username
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    conn = get_db_connection()
    machines = conn.execute('SELECT * FROM machines').fetchall()
    conn.close()
    return render_template('dashboard.html', machines=machines)

@app.route('/api/machines')
def api_machines():
    update_machine_status()
    conn = get_db_connection()
    machines = conn.execute('SELECT * FROM machines').fetchall()
    conn.close()
    data = [dict(m) for m in machines]
    return jsonify(data)

@app.route('/users', methods=['GET', 'POST'])
def users():
    if 'user' not in session:
        return redirect(url_for('login'))
    conn = get_db_connection()
    if request.method == 'POST':
        username = request.form['username']
        password = hashlib.sha256(request.form['password'].encode()).hexdigest()
        conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return render_template('users.html', users=users)

@app.route('/delete_user/<int:id>')
def delete_user(id):
    if 'user' not in session:
        return redirect(url_for('login'))
    conn = get_db_connection()
    conn.execute('DELETE FROM users WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('users'))

@app.route('/machines', methods=['GET', 'POST'])
def machines():
    if 'user' not in session:
        return redirect(url_for('login'))
    conn = get_db_connection()
    if request.method == 'POST':
        name = request.form['name']
        ip = request.form['ip']
        status = 'Connect'
        conn.execute('INSERT INTO machines (name, ip_address, status) VALUES (?, ?, ?)', (name, ip, status))
        conn.commit()
    machines = conn.execute('SELECT * FROM machines').fetchall()
    conn.close()
    return render_template('machines.html', machines=machines)

@app.route('/delete_machine/<int:id>')
def delete_machine(id):
    if 'user' not in session:
        return redirect(url_for('login'))
    conn = get_db_connection()
    conn.execute('DELETE FROM machines WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('machines'))

if __name__ == '__main__':
    app.run(debug=True)
