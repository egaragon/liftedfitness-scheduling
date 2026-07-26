from flask import Flask
from quickstart import main

app = Flask(__name__)

@app.route("/")

def index():
    return main()

