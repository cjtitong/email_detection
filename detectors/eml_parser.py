import extract_msg

def parse_eml(filepath):
    msg = extract_msg.Message(filepath)
    return {
        "subject": msg.subject,
        "body": msg.body,
        "sender": msg.sender
    }