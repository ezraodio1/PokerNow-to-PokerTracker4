import os
from src import monitor_folder

def main():
    downloads_folder = os.path.expanduser("~/Downloads")
    filename_pattern = "poker_now_log_"
    script_path = os.path.join(os.path.dirname(__file__), "src/pokernow_to_pokertracker.py")
    function_name = "pokernow_to_pokertracker"
    destination_folder = os.path.expanduser("~/Documents/Personal/Poker/Poker Script/poker_logs/pokernow_logs")

    monitor_folder(downloads_folder, filename_pattern, script_path, function_name, destination_folder)

if __name__ == "__main__":
    main()