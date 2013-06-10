import smtplib
from email.mime.text import MIMEText

class SMS:

    def __init__(self): 
        self.username = "kstonecipher.home@gmail.com"
        self.password = "20KelseyRocks10&"
        self.att_suffix = "@mms.att.net" # mobile.mycingular.com
        self.smtp_server = "smtp.gmail.com:587"

        self.emergency_numbers = ["8304601396"]
        self.emergency_message = "EMERGENCY"
        self.maintenence_numbers = ["8304601396"]
        self.maintenence_message = "Maintenence"


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
            phone_numbers[i] += "@mms.att.net" #mobile.mycingular.com"
         
        # Format message to look like an email
        # message["From"] = email_username
        # message["To"] = phone_number
        # message["Subject"] = "From your server!"
         
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
