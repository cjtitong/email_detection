# test_detector.py

import unittest
from email_simulator import send_email
from detector import is_malicious_email


class TestEmailDetection(unittest.TestCase):

    def test_simulated_malicious_email(self):
        subject = "Urgent Action Required"
        body = "Please click this link to get your free money: http://malicious-site.com"
        send_email(subject, body, "victim@example.com")

        # Here you'd retrieve the email from mailbox or parse it directly (if local)
        simulated_received_content = f"Subject: {subject}\n\n{body}"
        self.assertTrue(is_malicious_email(simulated_received_content))

    def test_simulated_safe_email(self):
        subject = "Weekly Update"
        body = "Hi, here's the weekly project update. Let me know your feedback."
        send_email(subject, body, "victim@example.com")

        simulated_received_content = f"Subject: {subject}\n\n{body}"
        self.assertFalse(is_malicious_email(simulated_received_content))


if __name__ == "__main__":
    unittest.main()