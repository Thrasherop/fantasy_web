# basic flask server


from flask import Flask, redirect, request, jsonify, render_template, send_file
import flask

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/downloads')
def dodododo_downloads():
    return render_template("downloads.html")

@app.route('/skycity')
def skycity():
    return render_template("skycity.html")

@app.route('/portfolio')
def portfolio():
    return render_template("portfolio.html")

@app.route('/github_redirect')
def github_redirect():
    return redirect("https://github.com/Thrasherop")

@app.route('/dodododo_download_all')
def dodododo_download_all():
    return send_file('misc/download_files/ALL-4-worlds.zip', as_attachment=True)


"""

World Download Links

"""
@app.route('/doodododo_download_disasterSMP')
def dodododo_download_disasterSMP():
    return send_file('misc/download_files/disasterSMPDirectory.zip', as_attachment=True)

@app.route('/doodododo_download_season_2-origins')
def dodododo_download_season_2_origins():
    return send_file('misc/download_files/dodododo_season_2-origins-.zip', as_attachment=True)

@app.route('/doodododo_download_skjafdkahesf')
def dodododo_download_skjafdkahesf():
    return send_file('misc\\download_files\\kjafdkahesfDirectory.zip', as_attachment=True)

@app.route('/doodododo_download_StillNotAmplified')
def dodododo_download_StillNotAmplified():
    return send_file('misc/download_files/StillNotAmplifiedDirectory.zip', as_attachment=True)


"""

Misc Endpoints

"""

@app.route('/file_download/ps1')
def file_download():
    return send_file('misc/misc_files/p.ps1', as_attachment=True)


if __name__ == "__main__":
    app.run(debug=False, port=80, host='0.0.0.0', threaded=True)

