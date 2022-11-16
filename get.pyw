import socket
import smtplib
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
s.ehlo()
s.starttls()
s.login('pixeltrading@outlook.com', 'YEWeyBn3PttehFD')
sender = "pixeltrading@outlook.com"
receivers = ["fabwellwal@gmail.com"]
subject = "SMTP e-mail Test" 
msg = "\nName: " + hostname + " Ip: " + ip
s.sendmail(sender, receivers, msg)
print ('sending email')
s.quit()