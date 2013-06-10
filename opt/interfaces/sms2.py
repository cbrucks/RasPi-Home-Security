import smtplib
from email.mime.text import MIMEText
 
# Message to be sent
message = MIMEText("Hello, texting!")
 
# Sending email username/password and receiving phone number
email_username = "kstonecipher.home"
email_password = "20KelseyRocks10&"
phone_number = "3618775020"
 
# Gmail to Verizon. Change here for different combinations.
email_username += "@gmail.com"
phone_number += "@mobile.mycingular.com"
 
# Format message to look like an email
message["From"] = email_username
message["To"] = phone_number
message["Subject"] = "From your server!"
 
# Connect and send
s = smtplib.SMTP('smtp.gmail.com:587')
s.starttls()
s.login(email_username, email_password)
s.sendmail(email_username, phone_number, message.as_string())
s.quit()
