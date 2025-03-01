from flask import Flask, request, jsonify, render_template_string
from googleapiclient.discovery import build
from transformers import pipeline
import re

app = Flask(__name__)

API_KEY = "AIzaSyCO9VG4-8i5TGZr6VuROa4pRbFgeHX1BNI"
youtube = build("youtube", "v3", developerKey=API_KEY)

# AI Models
sentiment_model = pipeline("sentiment-analysis")

def fetch_comments(video_id):
    comments = []
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100
    )
    response = request.execute()

    for item in response["items"]:
        comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        comments.append(comment)

    return comments

def generate_suggestions(comments):
    suggestions = []
    positive, negative = 0, 0

    for comment in comments:
        sentiment = sentiment_model(comment)[0]["label"]
        if sentiment == "POSITIVE":
            positive += 1
        else:
            negative += 1

    if positive > negative:
        suggestions.append("✅ Video ka Content Achha hai, More Interactive Q&A Add Karo")
    if negative > positive:
        suggestions.append("❌ Avoid Vulgar Language & Controversial Topics")
    if positive == 0:
        suggestions.append("👎 Add More Motivational & Positive Content")
    
    return suggestions

@app.route("/")
def index():
    html = open("index.html", "r").read()
    return render_template_string(html)

@app.route("/suggestions", methods=["POST"])
def suggestions():
    video_url = request.json["video_url"]
    video_id = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", video_url).group(1)

    comments = fetch_comments(video_id)
    if not comments:
        return jsonify({"suggestions": ["No Comments Found 😢"]})

    suggestions = generate_suggestions(comments)
    return jsonify({"suggestions": suggestions})

if __name__ == "__main__":
    app.run(debug=True)
