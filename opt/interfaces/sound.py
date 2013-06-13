import os
import ConfigParser
import pygame.mixer
from time import sleep
from sys import exit
import subprocess

class Sound:

    def __init__(self,config):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.button_sound  = BASE_DIR + "/" + config.get("Sound","button")
        self.armed_sound   = BASE_DIR + "/" + config.get("Sound","armed")
        self.alarm_sound   = BASE_DIR + "/" + config.get("Sound","alarm")
        self.warning_sound = BASE_DIR + "/" + config.get("Sound","warning")

    def _play_sound(self, fname):
        if ((fname.split('.'))[-1] == "wav") and (os.path.isfile(fname)):
            print fname
            subprocess.Popen(["aplay", fname])
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
    conf = ConfigParser.RawConfigParser()
    conf.readfp(open("../default.cfg"))
    sound = Sound(conf)
    print "playing"
    sound.play_warning_sound()
    sleep(1)
    sound.play_button_sound()
    sleep(1)
    sound.play_armed_sound()
    sleep(1)
    sound.play_alarm_sound()
    print "done"
