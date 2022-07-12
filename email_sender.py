import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()
ACCOUNT = os.getenv('GMAIL_ACCOUNT')
PASSWORD = os.getenv('GMAIL_PASSWORD')

FROM = os.getenv('GMAIL_ACCOUNT')
TO = "r.ozaki0318@gmail.com"

message = "Hello, this email is sending from python program."
msg = MIMEText(message, "html")
msg['Subject'] = "Hello from python"
msg["To"] = TO
msg["From"] = FROM

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(ACCOUNT, PASSWORD)
server.send_message(msg)
server.quit()