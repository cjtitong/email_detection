def is_malicious_email(content):
    keywords = ["free money", "click here", "urgent", "password expired"]
    return any(k in content.lower() for k in keywords)