# email_simulator.py

import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, to_email, from_email="test@local.com", smtp_server="localhost", smtp_port=1025):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.send_message(msg)
        print(f"Email sent to {to_email}")