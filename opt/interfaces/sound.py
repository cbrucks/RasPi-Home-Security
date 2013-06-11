import os
import ConfigParser

class Sound:

    def __init__(self,config):
        self.button_sound=config.get("Sound","button")
        self.armed_sound=config.get("Sound","armed")
        self.alarm_sound=config.get("Sound","alarm")
        self.warning_sound=config.get("Sound","warning")

    def _play_sound(self, fname):
        if ((fname.split('.'))[-1] == "mp3") and (os.path.isfile(fname)):
            os.system("mpg321 -q " + fname)
        else:
            raise Exception("File " + fname + " does not exist.")

    def play_button_sound(self):
        self._play_sound(self.button_sound)

    def play_armed_sound(self):
        self._play_sound(self.armed_sound)

    def play_alarm_sound(self):
        self._play_sound(self.alarm_sound)

    def play_warning_sound(self):
        self._play_sound(self.warning_sound)

if __name__ == "__main__":
    sound = Sound()
    sound.play_warning_sound()
    sound.play_button_sound()
    sound.play_armed_sound()
    sound.play_alarm_sound()
