# basic flask server


from flask import Flask, redirect, request, jsonify, render_template, send_file
import flask

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/dodododo_downloads')
def dodododo_downloads():
    return render_template("dodododo_downloads.html")

@app.route('/dodododo_download_all')
def dodododo_download_all():
    return send_file('misc/download_files/ALL-4-worlds.zip', as_attachment=True)


@app.route('/github_redirect')
def github_redirect():
    return redirect("https://github.com/Thrasherop")



if __name__ == "__main__":
    app.run(debug=True, port=80, host='0.0.0.0')

