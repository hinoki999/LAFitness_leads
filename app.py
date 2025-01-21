from flask import Flask, request, jsonify, send_from_directory
import sqlite3
from datetime import datetime
import os
import json

app = Flask(__name__)

# Initialize SQLite database
def init_db():
    conn = sqlite3.connect('leads.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS leads
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
         name TEXT NOT NULL,
         phone TEXT NOT NULL,
         email TEXT NOT NULL,
         timestamp TEXT NOT NULL,
         source TEXT,
         status TEXT DEFAULT 'new',
         assigned_to TEXT)
    ''')
    conn.commit()
    conn.close()

# Serve landing page
@app.route('/')
def landing_page():
    return send_from_directory('landing', 'index.html')

# API endpoint to collect leads
@app.route('/api/leads', methods=['POST'])
def collect_lead():
    data = request.json
    
    # Basic validation
    required_fields = ['name', 'phone', 'email']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400
    
    # Store lead in database
    conn = sqlite3.connect('leads.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO leads (name, phone, email, timestamp, source)
        VALUES (?, ?, ?, ?, ?)
    ''', (
        data['name'],
        data['phone'],
        data['email'],
        data.get('timestamp', datetime.now().isoformat()),
        data.get('source', 'direct')
    ))
    conn.commit()
    lead_id = c.lastrowid
    conn.close()
    
    # Simple notification (can be enhanced later)
    print(f"New lead received: {data['name']} ({data['phone']})")
    
    return jsonify({'success': True, 'lead_id': lead_id})

# Simple dashboard for salespeople
@app.route('/dashboard')
def dashboard():
    conn = sqlite3.connect('leads.db')
    c = conn.cursor()
    c.execute('SELECT * FROM leads ORDER BY timestamp DESC LIMIT 50')
    leads = c.fetchall()
    conn.close()
    
    # Convert to HTML table
    lead_rows = []
    for lead in leads:
        lead_rows.append(f"""
            <tr>
                <td>{lead[1]}</td>
                <td>{lead[2]}</td>
                <td>{lead[3]}</td>
                <td>{lead[4]}</td>
                <td>{lead[5]}</td>
                <td>{lead[6]}</td>
            </tr>
        """)
    
    return f"""
        <html>
            <head>
                <title>Leads Dashboard</title>
                <style>
                    table {{ border-collapse: collapse; width: 100%; }}
                    th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
                    th {{ background-color: #f2f2f2; }}
                </style>
            </head>
            <body>
                <h1>Recent Leads</h1>
                <table>
                    <tr>
                        <th>Name</th>
                        <th>Phone</th>
                        <th>Email</th>
                        <th>Timestamp</th>
                        <th>Source</th>
                        <th>Status</th>
                    </tr>
                    {''.join(lead_rows)}
                </table>
            </body>
        </html>
    """

if __name__ == '__main__':
    init_db()
    app.run(port=5000)