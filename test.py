import pyttsx3
import math

robot_mount = pyttsx3.init()


rate = robot_mount.getProperty('rate')
robot_mount.setProperty('rate', rate+50)

robot_mount.setProperty( 'voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
# 
    # 'voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices\Tokens\MSTTS_V110_viVN_An")


number = ["một", "hai", "ba", "bốn", "năm",
          "sáu", "bảy", "tám", "chín", "mười"]


for i in range(5):
    # robot_mount.say(number[i])
    robot_mount.say(number[i])
    # print(math.sqrt(i+1))
    robot_mount.runAndWait()



robot_mount.runAndWait()
