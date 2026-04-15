from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return {"message": "hello 3!"}

@app.route("/api", methods=["POST"])
def sentiment():
    body_data = request.get_json()
    print("Body data:")
    print(body_data["data"])
    return {"message": "hello from api"}

