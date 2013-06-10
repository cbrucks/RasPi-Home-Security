import os

class Sound:

    def __init__(self):
        pass

    def _play_sound(self, fname):
        if ((fname.split('.'))[-1] == "mp3") and (os.path.isfile(fname)):
            os.system("mpg321 -q " + fname)
        else:
            raise Exception("File " + fname + " does not exist.")

    def play_button_sound(self):
        BUTTON_SOUND = "sounds/button_press/button1.mp3"
        self._play_sound(BUTTON_SOUND)

    def play_armed_sound(self):
        ARMED_SOUND = "sounds/armed/armed.mp3"
        self._play_sound(ARMED_SOUND)

    def play_alarm_sound(self):
        ALARM_SOUND = "sounds/alarm/alarm1.mp3"
        self._play_sound(ALARM_SOUND)

if __name__ == "__main__":
    sound = Sound()
    sound.play_button_sound()
    sound.play_armed_sound()
    sound.play_alarm_sound()
