from flask import Flask, render_template, request
import speech_recognition as sr
from gtts import gTTS
import os
from datetime import date, datetime
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Tải tài nguyên phân tích cảm xúc
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

# Khởi tạo ứng dụng Flask
app = Flask(__name__)

# Trang chủ
@app.route('/')
def home():
    return render_template('index.html')

# Xử lý dữ liệu từ form
@app.route('/process', methods=['POST'])
def process():
    # Nhận dữ liệu từ form HTML
    user_input = request.form['user_input']
    
    # Xử lý nhận diện giọng nói và cảm xúc
    robot_brain = ""
    sentiment_score = sia.polarity_scores(user_input)
    
    if "chào" in user_input:
        robot_brain = "Chào bạn! Bạn cảm thấy thế nào hôm nay?"
    elif "buồn" in user_input or sentiment_score['compound'] < -0.2:
        robot_brain = "Tôi rất tiếc khi nghe điều đó. Bạn muốn chia sẻ thêm không?"
    elif "vui" in user_input or sentiment_score['compound'] > 0.2:
        robot_brain = "Thật tuyệt khi nghe điều đó! Bạn đã làm gì vui hôm nay?"
    elif "nay" in user_input:
        today = date.today()
        robot_brain = today.strftime("Hôm nay là ngày %d tháng %m năm %Y")
    elif "giờ" in user_input:
        now = datetime.now()
        robot_brain = now.strftime("Bây giờ là %H giờ %M phút %S giây")
    else:
        robot_brain = "Tôi không hiểu bạn nói gì."

    # Text-to-Speech (nếu cần phát ra âm thanh)
    tts = gTTS(robot_brain, lang="vi")
    tts.save("response.mp3")
    os.system("start response.mp3")

    # Trả kết quả lại cho trang result.html
    return render_template('result.html', output=robot_brain)

if __name__ == '__main__':
    app.run(debug=True)
