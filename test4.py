import speech_recognition as sr
from gtts import gTTS
import os
from datetime import date, datetime
import sys
import locale

# Đặt mã hóa đầu ra thành UTF-8
sys.stdout.reconfigure(encoding='utf-8')
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

# Khởi tạo bộ nhận diện giọng nói
robot_ear = sr.Recognizer()

# Biến lưu trữ câu trả lời của robot
robot_brain = ""

while True:
    with sr.Microphone() as mic:
        print("Robot: Tôi đang lắng nghe...")
        audio = robot_ear.record(mic, duration=5)

    print("Robot: Đang xử lý...")

    try:
        # Nhận diện giọng nói tiếng Việt
        you = robot_ear.recognize_google(audio, language="vi-VN")
    except Exception as e:
        print(f"Lỗi khi nhận diện giọng nói: {e}")
        you = ""

    print("Bạn: " + you)

    # Xử lý câu trả lời dựa trên đầu vào
    if you == "":
        robot_brain = "Tôi không nghe rõ."
    elif "chào" in you:
        robot_brain = "Chào bạn!"
    elif "nay" in you:
        today = date.today()
        robot_brain = today.strftime("Hôm nay là ngày %d tháng %m năm %Y")
    elif "giờ" in you:
        now = datetime.now()
        robot_brain = now.strftime("Bây giờ là %H giờ %M phút %S giây")
    elif "tạm biệt" in you:
        robot_brain = "Tạm biệt! Chúc bạn một ngày tốt lành!"
    else:
        robot_brain = "Tôi không hiểu bạn nói gì."

    # In câu trả lời của robot
    print("Robot: " + robot_brain)

    # Phát âm tiếng Việt bằng Google Text-to-Speech
    tts = gTTS(robot_brain, lang="vi")
    tts.save("response.mp3")
    
    # Phát âm thanh
    tts = gTTS(robot_brain, lang="vi")
    tts.save("response.mp3")
    os.system("start response.mp3")
 
    # Xóa file âm thanh sau khi phát
    try:
        os.remove("response.mp3")
        print(f"Đã xóa file âm thanh: response.mp3")
    except OSError as e:
        print(f"Lỗi khi xóa file: {e}")

    # Nếu robot chào tạm biệt, thoát khỏi vòng lặp
    if "tạm biệt" in you:
        break
