import smtplib
import mimetypes
import email
import email.mime.application
import sys
import ConfigParser
import json

class Email_Conductor:
    def __init__(self, config):
        self.email = config.get("SMTP","email")
        self.password = config.get("SMTP","password")
        self.smtp_server = config.get("SMTP","server")

        self.emergency_emails = config.get("Emergency","emails").split(",")
        self.emergency_email_subject = config.get("Emergency","subject")
        self.emergency_email_body = config.get("Emergency","body")

        self.maintenence_emails = config.get("Maintenence","emails").split(",")
        self.maintenence_email_subject = config.get("Maintenence","subject")
        self.maintenence_email_body = config.get("Maintenence", "body")


    def _send_email(self, to_addr=[], subject="", body="""""", files=[]): 
        # TODO check email addresses for validity
                

        # TODO check to see if files exist


        # Create a text/plain message
        msg = email.mime.Multipart.MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = self.email        # 'me@example.com'
        msg['To'] = ','.join(to_addr)   # ['you@example.com','you.too@gmail.com']
     
        # The main body is just another attachment
        body = email.mime.Text.MIMEText(body)
        msg.attach(body)
     
    
        for fqfn in files:
           # Extract the filename from the fully quailfied file name
           spl_dir = fqfn.split('/')
           filename = spl_dir[-1]
     
           # Extract the file type from the filename
           spl_type = filename.split('.')
           file_type = spl_type[-1]
     
           # Open the file in binary mode to attach to the email
           file_contents = open(fqfn,'rb')
           attachment = email.mime.application.MIMEApplication(file_contents.read(), _subtype=file_type)
           file_contents.close()
           attachment.add_header('Content-Disposition', 'attachment', filename=filename)
           msg.attach(attachment)
     
        # send via Gmail server
        # NOTE: my ISP, Centurylink, seems to be automatically rewriting
        # port 25 packets to be port 587 and it is trashing port 587 packets.
        # So, I use the default port 25, but I authenticate.
        s = smtplib.SMTP(self.smtp_server)
        s.starttls()
        s.login(self.email, self.password)
        s.sendmail(self.email, to_addr, msg.as_string())
        s.quit()


    def send_emergency_email(self, files=[]):
        self._send_email(self.emergency_emails, self.emergency_email_subject, self.emergency_email_body, files)


    def send_maintenence_email(self, files=[]):
        self._send_email(self.maintenence_emails, self.maintenence_email_subject, self.maintenence_email_body, files)


if __name__=="__main__":
    email_conductor = Email_Conductor()
    email_conductor.send_emergency_email(["/home/pi/python_games/gem1.png","/home/pi/python_games/gem2.png"])
    email_conductor.send_maintenence_email(["/home/pi/python_games/gem3.png"])
