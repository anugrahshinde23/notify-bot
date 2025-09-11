from flask import Flask, request, send_file
from gtts import gTTS
import io



app = Flask(__name__)

# Predefined Q&A
qa_pairs = {
    "what is notice app": "Notice app is a platform for students and teachers to share important updates.",
    "who made this app": "This app was created by Anugrah Shinde.",
    "what is flutter": "Flutter is a framework for building cross-platform apps.",
    "how can i check new notices" : "On the home screen you will see the latest notices, pull down to refresh for new updates or try switching the screens",
    "how can i check profile" : "At top left corner",
    "how do i post a new notice" : "Go to homescreen add your details choose file (if any) and post notice",
    "can i edit or delete a notice" : "Yes, you can edit and notices from notice sections tap on notices tab",
    "how will student receive my notice" : "By notification",
    "how do i use this app" : "Just register if your not then simply choose your college and class and then click complete registration and see the notices posted by your teachers"
}

# Text-to-speech (direct memory, no file)
def text_to_speech(text):
    tts = gTTS(text=text, lang="en")
    mp3_fp = io.BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    return mp3_fp

@app.route("/start", methods=["GET"])
def start_bot():
    welcome_text = "Hey, I'm Ruth your AI assistant thoughtfully created by Anugrah Shinde to guide, support and simplify your experience"
    audio_stream = text_to_speech(welcome_text)
    return send_file(audio_stream, mimetype="audio/mpeg")

@app.route("/ask", methods=["POST"])
def ask_bot():
    data = request.json
    question = data.get("question", "").lower().strip()

    if question in qa_pairs:
        answer = qa_pairs[question]
    else:
        answer = "Sorry, I cannot answer that. Goodbye."

    audio_stream = text_to_speech(answer)
    return send_file(audio_stream, mimetype="audio/mpeg")



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
