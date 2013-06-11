import smtplib
from email.mime.text import MIMEText
import ConfigParser

class SMS:

    def __init__(self, config): 
        self.username = config.get("SMTP","email")
        self.password = config.get("SMTP","password")
        self.att_suffix = config.get("SMTP","att_suffix")
        self.smtp_server = config.get("SMTP","server")

        self.emergency_numbers = config.get("Emergency","phone_numbers").split(",")
        self.emergency_subject = config.get("Emergency","subject")
        self.emergency_message = config.get("Emergency","body")
        self.maintenence_numbers = config.get("Maintenence","phone_numbers").split(",")
        self.maintenence_subject = config.get("Maintenence","subject")
        self.maintenence_message = config.get("Maintenence","body")


    def _send_sms(self, phone_numbers=[], message=''):
        # Verify the phone numbers
        if not phone_numbers:
            raise Exception("Recipient Phone Number list can not be empty!")
            return
        for number in phone_numbers:
            if len(number) != 10:
                raise Exception("Phone Number, "+number+", is not valid! Incorrect length.")
                return

        # Message to be sent
        msg = MIMEText(message)
         
        # Gmail to Verizon. Change here for different combinations.
        for i,number in enumerate(phone_numbers):
            phone_numbers[i] += self.att_suffix
         
        # Format message to look like an email
        # message["From"] = email_username
        # message["To"] = phone_number
        msg["Subject"] = self.maintenence_subject
         
        # Connect and send
        s = smtplib.SMTP(self.smtp_server)
        s.starttls()
        s.login(self.username, self.password)
        s.sendmail(self.username, phone_numbers, msg.as_string())
        s.quit()


    def send_emergency_sms(self):
        self._send_sms(self.emergency_numbers, self.emergency_message)

    def send_maintenence_sms(self):
        self._send_sms(self.maintenence_numbers, self.maintenence_message)


if __name__ == "__main__":
    sms = SMS()
    sms.send_emergency_sms()
    sms.send_maintenence_sms() 
