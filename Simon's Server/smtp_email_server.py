import smtplib
import random
import csv
from email import encoders, message
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()

with open('Data/password.txt', 'r') as file:
    pw = file.read()

admin = 'admin@gmail.com' # Hypothetic Email
server.login(admin, pw)
msg = MIMEMultipart()

names, emails = [], []
csv_path = 'Data\info.csv'
with open(csv_path, 'r') as file:
    lines = csv.reader(file)
    
    for line in lines:
        names.append(line[0])
        emails.append(line[1])
print(f'Recipients: {names}')
print(f'Recipient Emails: {emails}')

with open('Data/message.txt', 'r') as file:
    message = file.read()

for i in range(len(names)):
    msg = MIMEMultipart()
    msg['From'] = admin
    msg['To'] = emails[i]
    msg['Subject'] = 'Sorry For Interruption' # Email Header  

    msg.attach(MIMEText(message, 'plain'))
    num = random.randint(1, 3)
    filename = 'Data/meme'+str(num)+'.jpg'
    attachment = open(filename, 'rb')

    temp = MIMEBase('application', 'octet-stream')
    temp.set_payload(attachment.read())
    encoders.encode_base64(temp)
    temp.add_header('Content-Disposition', f'attachment; filename={filename}')
    msg.attach(temp)

    text = msg.as_string()
    server.sendmail(admin, emails[i], text)
print('All Emails Have Been Sent')




