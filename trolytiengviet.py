import os
import time 
import playsound
import pyttsx3
import speech_recognition 
from gtts import gTTS 
from calculate_age import calculateAge
from datetime import date
# from pygame import mixer
from homnaythumay import getDayOfWeek
from google_calendar_api import get_google_calendar_events, google_calendar_service
'''
không làm cái này nữa vì quá lâu
'''

# //remove 2 file kia
# os.remove("speech1.mp3") 
# os.remove("speech0.mp3")

def listInString(a, string):
    string = string.split(" ")
    for i in a:
        if i not in string:
            return False
    return True 

count = 0
def speak(data):
    global count
    tts = gTTS(text=data, lang="vi")
    tts.save(f'speech{count%10000}.mp3')

    playsound.playsound(f'speech{count%10000}.mp3')
    # mixer.init()
    # mixer.music.load(f'speech{count%2}.mp3')
    # mixer.music.play()
    print("Trợ lý: " + data)
    count += 1
    # print("Đang trả lời...")
    # playsound.playsound("voice.mp3")
    # print("Assistance: " + data)
    
def getAudio():
    robot_ear = speech_recognition.Recognizer()  # speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        print("Đang nghe...")
        audio = robot_ear.listen(mic)

    said = ""
    try:
        # speech_recognition.Recognizer().recognize_google
        said = robot_ear.recognize_google(audio, language="vi-VN")
        print("Bạn: " + said)
    except Exception as e :
        print("Bạn: không xác định!")
        print("Exception: "+ str(e))

    return said

#get input sound 

number = ["một", "hai", "ba", "bốn", "năm",
          "sáu", "bảy", "tám", "chín", "mười"]
#response

def start():
    myTextSound = ""
    input("Enter để bắt đầu: ")
    while("thoát" not in myTextSound):
        myTextSound  = getAudio().lower()
        if "thoát" in myTextSound:
            break
        if listInString(["bạn", "tuổi"], myTextSound):
            yearOld = calculateAge(date(2020, 11, 14))
            speak("tuổi của tôi là "+ str(yearOld) + " vì tôi được lập trình vào ngày mười bốn, tháng mười một, năm hai không hai mươi")
        elif("lô" in myTextSound):
            speak("lô con cặc")
        elif(listInString(["chào"],myTextSound) ):
            speak("chào bạn")
        elif(myTextSound == ""):
            print("vui lòng nói lại!"); 
        elif  listInString(["nay", "thứ"], myTextSound) :
            speak(getDayOfWeek())
        elif listInString(["sắp", "có"], myTextSound) : #sắp tới có những gì? sắp có những gì,    
            service = google_calendar_service()
            Events = get_google_calendar_events(20, service);
            for event in Events:
                speak("vào ngày " + event[0][2] + " tháng " + event[0][1] + " năm " + event[0][0] + " bạn phải " + event[2] )
                # speak(event[2])
                # speak("và")
        else:
            print("Vui lòng nói lại!")

        input("Enter để tiếp tục: ")


start()
# for i in range(100):
    # speak(str(i)); 
print("Xong chương trình")