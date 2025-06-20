# detector.py

import re

def is_malicious_email(content: str) -> bool:
    patterns = [
        r"https?:\/\/[^\s]+",
        r"free money|urgent action",
        r"attachment\.exe|\.scr"
    ]
    return any(re.search(p, content, re.IGNORECASE) for p in patterns)