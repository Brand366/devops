from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["POST"])
def index():
        print(str(request.data))
        print("Got message from github")
        return "Build Server"
