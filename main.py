# basic flask server


from flask import Flask, request, jsonify, render_template
import flask

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/downloads')
def downloads():
    return render_template("downloads.html")


if __name__ == "__main__":
    app.run(debug=True, port=5705, host='0.0.0.0')

