from flask import Flask, request
app = Flask(__name__)

@app.route("getProblem.py", methods=["GET"])
def pythonAjaxTest():
    return("Hello World")
