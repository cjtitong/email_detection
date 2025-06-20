def is_suspicious_file(filename):
    suspicious_extensions = [".exe", ".bat", ".vbs", ".scr"]
    return any(filename.lower().endswith(ext) for ext in suspicious_extensions)