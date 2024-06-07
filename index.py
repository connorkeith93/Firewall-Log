import argparse
import csv
from log_analyzer import LogEntry

def print_head(log_entries):
    """
    Print the first 5 objects from the list of LogEntry objects.
    """
    for i in range(min(5, len(log_entries))):
        log_entry = log_entries[i]
        print("Date:", log_entry.event_time.strftime("%m/%d/%Y %H:%M %Z"))
        print("Action:", log_entry.action)
        print("Source IP:", log_entry.source_ip)
        print("IPv4 Class:", log_entry.ipv4_class)
        print("Country Name:", log_entry.country_name)
        print("-------------------------")

def deny_count(log_entries):
    """
    Count the number of log entries with action "Deny".
    """
    denied_logs = [log_entry for log_entry in log_entries if log_entry.action == "Deny"]
    num_denied = len(denied_logs)
    print(f"{num_denied} log entries were denied.")

def country_count(log_entries, country_code):
    """
    Count the number of log entries from a specific country.
    """
    country_logs = [log_entry for log_entry in log_entries if log_entry.country == country_code]
    num_country_logs = len(country_logs)
    print(f"{num_country_logs} log entries from {country_code} were recorded.")

def main():
    # Set up argument parser to handle command line inputs
    parser = argparse.ArgumentParser(description="Firewall Log Analyzer")
    parser.add_argument("--filename", "-f", required=True, help="Path to the CSV file")
    parser.add_argument("--action", "-a", required=True, help="Action to perform: 'head' to print first 5 entries, 'deny' to count denied entries, 'source' to count entries from a specific country")
    parser.add_argument("--country", "-c", help="2-letter country code to filter log entries")
    args = parser.parse_args()

    # Retrieve command line arguments
    filename = args.filename
    action = args.action
    country_code = args.country

    # Read data from the CSV file
    log_entries = []
    with open(filename, mode="r", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            # Create a LogEntry object for each row in the CSV file
            log_entry = LogEntry(
                row["event_time"],
                row["internal_ip"],
                row["port_number"],
                row["protocol"],
                row["action"],
                row["rule_id"],
                row["source_ip"],
                row.get("country"),
                row.get("country_name")
            )
            # Add the log entry to the list
            log_entries.append(log_entry)

    # Perform action based on user input
    if action == "head":
        print_head(log_entries)
    elif action == "deny":
        deny_count(log_entries)
    elif action == "source" and country_code:
        country_count(log_entries, country_code)
    else:
        print("Invalid action. Please use 'head', 'deny', or 'source' with a valid --country code.")

if __name__ == "__main__":
    main()
