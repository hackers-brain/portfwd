import json
import os
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# os.system("./ngrok http 80")
os.system("./ngrok http 80 > /dev/null &")
time.sleep(10)
os.system("curl http://localhost:4040/api/tunnels > tunnels.json")

with open('tunnels.json') as data_file:
    datajson = json.load(data_file)


msg = "\t\tngrok URL's: \n\n"
for i in datajson['tunnels']:
    msg = msg + i['public_url'] + '\n'

# print(msg)


mail_content = f""" \t\t RPI Server Details...
\t{msg}"""
sender_address = "example@email.com"
sender_pass = "password"
destination_mail = "example@email.com"

message = MIMEMultipart()
message['From'] = " RPI Server"
message['To'] = destination_mail
message['Subject'] = " Port Forwarded Details..."

message.attach(MIMEText(mail_content, 'plain'))

session = smtplib.SMTP_SSL('smtp.gmail.com')
session.connect('smtp.gmail.com', 465)
session.login(sender_address, sender_pass)
text = message.as_string()
session.sendmail(sender_address, destination_mail, text)
session.quit()
# print(" Mail Sent !!!")
