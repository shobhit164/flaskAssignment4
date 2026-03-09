from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    message = os.getenv("APP_MESSAGE", "Hello from Flask!")
    return message

@app.route("/health")
def health():
    health_message = os.getenv("APP_HEALTH", "App is healthy")
    return health_message

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)