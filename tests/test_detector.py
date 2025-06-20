import unittest
from detectors.email_detector import is_malicious_email
from detectors.file_scanner import is_suspicious_file

class TestDetection(unittest.TestCase):

    def test_email_detection(self):
        self.assertTrue(is_malicious_email("free money now"))
        self.assertFalse(is_malicious_email("project update"))

    def test_file_scanner(self):
        self.assertTrue(is_suspicious_file("trojan.exe"))
        self.assertFalse(is_suspicious_file("report.pdf"))

if __name__ == "__main__":
    unittest.main()