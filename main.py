from simulator.email_simulator import send_email

EMAIL_USER = "local@test.com"
VT_API_KEY = None

def is_malicious_email(email_body):
    # Dummy logic for testing
    return "free money" in email_body.lower()

def is_suspicious_file(filename):
    # Dummy logic for testing
    return filename.endswith(".exe")

if __name__ == "__main__":
    print(f"Email user loaded: {EMAIL_USER}")
    print(f"VirusTotal API key loaded: {VT_API_KEY}")

    sample_email = "Click here to win free money!"
    if is_malicious_email(sample_email):
        print("[ALERT] Malicious email detected.")

    sample_file = "invoice.exe"
    if is_suspicious_file(sample_file):
        print("[ALERT] Suspicious attachment detected.")

    # Call send_email function to send test email through debug SMTP server
    send_email(
        subject="Test Email",
        body="This is a test email for detection.",
        recipient="alexccalvert28@gmail.com"
    )
    print("Email sent to alexccalvert28@gmail.com (debug server)")