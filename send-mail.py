import smtplib
from email.mime.text import MIMEText

f = open('info.txt')
lines = f.readlines()

sender = lines[4]
recipient = lines[4]
subject = lines[10]
text = MIMEText(u+lines[13], 'html')
passw = lines[7]

text['Subject'] = subject
text['From'] = sender
text['To'] = recipient

server = smtplib.SMTP('smtp.gmail.com')
server.starttls()
server.login(sender,passw)
server.sendmail(sender, [recipient], text.as_string())
server.quit()
