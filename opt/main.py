import os
import ConfigParser

from interfaces.sound import Sound
from interfaces.ip import IP
from interfaces.email_conductor import Email_Conductor
from interfaces.sms import SMS


def func(string,sleep,sound):
    sound.play_alarm_sound()
    

if __name__ == "__main__":
    # Read in the configuration file\
    user_config = 'conf.cfg'
    config = ConfigParser.RawConfigParser()
    config.readfp(open('default.cfg'))
    if os.path.isfile(user_config):
        config.read(user_config)


    ip = IP()
    sound = Sound(config)
    email_conductor = Email_Conductor(config)
    sms = SMS(config)

    sound.play_button_sound()
    sound.play_warning_sound()
    sound.play_armed_sound()
    sound.play_alarm_sound()
    sleep(1)
#     email_conductor.send_emergency_email()
#     email_conductor.send_maintenence_email()
# 
#     sms.send_emergency_sms()
#     sms.send_maintenence_sms()
