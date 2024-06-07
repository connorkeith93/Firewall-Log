import unittest
from log_analyzer import LogEntry

class TestLogEntry(unittest.TestCase):
    def test_event_time_conversion(self):
        # Test case 1: Ensure event_time string is properly converted to a datetime object
        log_entry = LogEntry("2022-01-01 08:29:25 UTC", "", "", "", "", "", "")
        self.assertEqual(log_entry.event_time.month, 1)  # Check if month is equal to 1
        self.assertEqual(log_entry.event_time.hour, 8)   # Check if hour is equal to 8

        # Additional test cases can be added here if needed

    def test_ipv4_class(self):
        # Test case 2: Ensure ipv4_class returns the correct IPv4 address class
        log_entry_A = LogEntry("2022-01-01 08:29:25 UTC", "", "", "", "", "", "11.177.69.220")
        log_entry_B = LogEntry("2022-01-01 08:29:25 UTC", "", "", "", "", "", "173.205.219.112")
        log_entry_C = LogEntry("2022-01-01 08:29:25 UTC", "", "", "", "", "", "192.168.1.1")
        log_entry_D = LogEntry("2022-01-01 08:29:25 UTC", "", "", "", "", "", "229.163.4.51")

        self.assertEqual(log_entry_A.ipv4_class, "A")  # Check if ipv4_class returns "A" for source_ip "11.177.69.220"
        self.assertEqual(log_entry_B.ipv4_class, "B")  # Check if ipv4_class returns "B" for source_ip "173.205.219.112"
        self.assertEqual(log_entry_C.ipv4_class, "C")  # Check if ipv4_class returns "C" for source_ip "192.168.1.1"
        self.assertEqual(log_entry_D.ipv4_class, "D")  # Check if ipv4_class returns "D" for source_ip "229.163.4.51"

        # Additional test cases can be added here if needed

if __name__ == "__main__":
    unittest.main()
