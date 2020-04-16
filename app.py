import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Test_okd_build!"

@app.route("/test")
def hello():
    return "Test is complete"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
