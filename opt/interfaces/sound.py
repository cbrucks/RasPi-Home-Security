import os

def _play_sound(fname):
    if ((fname.split('.'))[-1] == "mp3") and (os.path.isfile(fname)):
        os.system("mpg321 -q " + fname +" 2>&1 > logfile &")
    else:
        raise Exception("File " + fname + " does not exist.")

def play_button_sound():
    BUTTON_SOUND = "sounds/button_press/button1.mp3"
    _play_sound(BUTTON_SOUND)

def play_armed_sound():
    ARMED_SOUND = "sounds/armed/armed.mp3"
    _play_sound(ARMED_SOUND)

def play_alarm_sound():
    ALARM_SOUND = "sounds/alarm/alarm1.mp3"
    _play_sound(ALARM_SOUND)

play_button_sound()
play_armed_sound()
play_alarm_sound()
