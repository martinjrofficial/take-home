from flask import Flask
import socket
import datetime

app = Flask(__name__)

@app.route('/')
def get_info():
    timestamp = datetime.datetime.now().isoformat()
    hostname = socket.gethostname()
    return f"Timestamp: {timestamp}\nHostname: {hostname}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)