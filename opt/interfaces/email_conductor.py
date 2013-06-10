import smtplib
import mimetypes
import email
import email.mime.application
import sys

class Email_Conductor:
    def _send_email(self, to_addr, from_addr, from_pwd, subject="", body="""""", files=[]): 
        # Create a text/plain message
        msg = email.mime.Multipart.MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = from_addr         # 'me@example.com'
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
        s = smtplib.SMTP('smtp.gmail.com:587')
        s.starttls()
        s.login(from_addr, from_pwd)
        s.sendmail(from_addr, to_addr, msg.as_string())
        s.quit()


if __name__=="__main__":
    email_conductor = Email_Conductor()
    email_conductor._send_email(["chris.brucks@rackspace.com","treflipmaster@gmail.com"], "kstonecipher.home@gmail.com", "20KelseyRocks10&", "Python Email Test", "This is a test email with attached pictures.", ["/home/pi/python_games/gem1.png","/home/pi/python_games/gem2.png"])
