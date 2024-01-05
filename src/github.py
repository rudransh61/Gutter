import argparse
import os
import json
from datetime import datetime

# Constants
ANALYTICS_FILE = "cli_analytics.json"

def record_analytics(command):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Load existing analytics data or create a new dictionary
    if os.path.exists(ANALYTICS_FILE):
        with open(ANALYTICS_FILE, "r") as file:
            analytics_data = json.load(file)
    else:
        analytics_data = {}

    # Update analytics data with the new command usage
    if command in analytics_data:
        analytics_data[command]["count"] += 1
        analytics_data[command]["last_used"] = timestamp
    else:
        analytics_data[command] = {"count": 1, "last_used": timestamp}

    # Save updated analytics data
    with open(ANALYTICS_FILE, "w") as file:
        json.dump(analytics_data, file, indent=2)

def parse_arguments():
    parser = argparse.ArgumentParser(description="CLI Analytics Tool")
    parser.add_argument("command", help="The CLI command to track")
    return parser.parse_args()

def main():
    args = parse_arguments()
    record_analytics(args.command)
    print(f"Command '{args.command}' recorded in analytics.")

if __name__ == "__main__":
    main()
