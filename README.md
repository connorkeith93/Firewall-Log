# Firewall-Log

This repository contains a Firewall Log Analyzer tool that processes firewall log entries from a CSV file. The tool provides functionality to print the first few log entries, count the number of denied entries, and count entries from a specific country. The repository includes the following files:

- `index.py`: The main script that handles command-line arguments, reads the CSV file, and performs the specified analysis action.
- `log_analyzer.py`: Contains the `LogEntry` class, which represents individual log entries with attributes such as event time, action, source IP, country, and more.
- `test_log_analyzer.py`: A set of tests to ensure the functionality of the `LogEntry` class and the main script.

## How It Works

1. **index.py**:
   - Parses command-line arguments to determine the action to perform and the CSV file to read.
   - Reads the CSV file and creates `LogEntry` objects for each row.
   - Performs the specified action:
     - `head`: Prints the first 5 log entries.
     - `deny`: Counts and prints the number of log entries with the action "Deny".
     - `source`: Counts and prints the number of log entries from a specified country.

2. **log_analyzer.py**:
   - Defines the `LogEntry` class with attributes such as event time, action, source IP, country, etc.
   - Provides methods to process and analyze individual log entries.

3. **test_log_analyzer.py**:
   - Contains unit tests to verify the correctness of the `LogEntry` class and the main script's functionality.

## Usage

To use the Firewall Log Analyzer, run the `index.py` script with the appropriate command-line arguments:

```bash
python index.py --filename <path_to_csv> --action <action> [--country <country_code>]
