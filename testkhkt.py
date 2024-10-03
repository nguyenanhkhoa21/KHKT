import speech_recognition as sr
from gtts import gTTS
import os
from datetime import date, datetime
import sys
import locale
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
sys.stdout.reconfigure(encoding='utf-8')
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
robot_ear = sr.Recognizer()
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()
robot_brain = ""
conversation_log = []
while True:
    with sr.Microphone() as mic:
        print("Robot: Tôi đang lắng nghe...")
        audio = robot_ear.record(mic, duration=15)
    print("Robot: Đang xử lý...")
    try:
        you = robot_ear.recognize_google(audio, language="vi-VN")
    except Exception as e:
        print(f"Lỗi khi nhận diện giọng nói: {e}")
        you = ""
    print("Bạn: " + you)
    conversation_log.append(f"Bạn: {you}")
    sentiment_score = sia.polarity_scores(you)
    if you == "":
        robot_brain = "Tôi không nghe rõ."
    elif "chào" in you:
        robot_brain = "Chào bạn! Bạn cảm thấy thế nào hôm nay?"
    elif "tôi buồn" in you or sentiment_score['compound'] < -0.2:
        robot_brain = "Tôi rất tiếc khi nghe điều đó. Bạn muốn chia sẻ thêm không?"
    elif "tôi vui" in you or sentiment_score['compound'] > 0.2:
        robot_brain = "Thật tuyệt khi nghe điều đó! Bạn đã làm gì vui hôm nay?"
    elif "nay" in you:
        today = date.today()
        robot_brain = today.strftime("Hôm nay là ngày %d tháng %m năm %Y")
    elif "giờ" in you:
        now = datetime.now()
        robot_brain = now.strftime("Bây giờ là %H giờ %M phút %S giây")
    elif "tạm biệt" in you:
        robot_brain = "Tạm biệt! Chúc bạn một ngày tốt lành!"
        print("Robot: " + robot_brain)
        tts = gTTS(robot_brain, lang="vi")
        tts.save("response.mp3")
        os.system("start response.mp3")
        break
    else:
        robot_brain = "Tôi không hiểu bạn nói gì."
    print("Robot: " + robot_brain)
    conversation_log.append(f"Robot: {robot_brain}")
    tts = gTTS(robot_brain, lang="vi")
    tts.save("response.mp3")
    os.system("start response.mp3")
with open("conversation_log.txt", "w", encoding="utf-8") as f:
    for line in conversation_log:
        f.write(line + "\n")
print("Cuộc trò chuyện đã được ghi lại.")
