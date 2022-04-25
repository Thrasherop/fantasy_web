# basic flask server


from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

@app.route('/')
def index():
    return "hello world"

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True, port=5705)

