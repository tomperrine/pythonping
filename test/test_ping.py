import unittest
from pythonping import ping


class PingCase(unittest.TestCase):
    """Tests for actual ping against localhost"""

    def test_ping_execution(self):
        """Verifies that random_text generates text of correct size"""
        # NOTE, this may be considered an e2e test
        self.assertEqual(len(ping('10.127.0.1', count=4, size=10)), 4,
                         'Sent 4 pings to localhost, but not received 4 responses')
