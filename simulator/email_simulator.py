import smtplib
from email.message import EmailMessage

def send_email(subject, body, recipient):
    msg = EmailMessage()
    msg['From'] = 'sender@example.com'
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.set_content(body)

    try:
        # Connect to local debug SMTP server (e.g., aiosmtpd)
        server = smtplib.SMTP('localhost', 1026)  # Make sure this port matches your aiosmtpd port
        server.send_message(msg)
        server.quit()
        print(f"Email sent to {recipient} (debug server)")
    except ConnectionRefusedError:
        print("[ERROR] Could not connect to debug SMTP server. Is it running on port 1026?")