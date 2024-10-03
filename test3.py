import speech_recognition as sr
import pyttsx3
from datetime import date, datetime

# Khởi tạo bộ nhận diện giọng nói và bộ phát giọng nói
robot_ear = sr.Recognizer()
robot_mouth = pyttsx3.init()

# Tùy chỉnh tốc độ giọng nói
robot_mouth.setProperty('rate', 150)

# Chọn giọng nói tiếng Việt
# Chọn giọng nói tiếng Việt
voices = robot_mouth.getProperty('voices')
for voice in voices:
    if 'vi' in voice.languages:
        robot_mouth.setProperty('voice', voice.id)
        break

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
    except:
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
        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else:
        robot_brain = "Tôi không hiểu bạn nói gì."

    # In và phát âm câu trả lời của robot
    print("Robot: " + robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
