from flask import Flask, jsonify
import os
from datetime import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get user information
    name = "Raj Gaur"  # Replace with your full name
    username = os.getlogin()  # Get system username
    
    # Get server time in IST
    server_time_ist = datetime.now().astimezone().isoformat()
    
    # Get top command output
    top_output = subprocess.run(['top', '-b', '-n', '1'], capture_output=True, text=True).stdout

    return f"""
    <html>
        <head><title>HTOP Info</title></head>
        <body>
            <h1>System Information</h1>
            <p>Name: {name}</p>
            <p>Username: {username}</p>
            <p>Server Time (IST): {server_time_ist}</p>
            <pre>{top_output}</pre>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
