import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import importlib.util

class DownloadEventHandler(FileSystemEventHandler):
    def __init__(self, pattern, script_path, function_name, destination_folder):
        self.pattern = pattern
        self.script_path = script_path
        self.function_name = function_name
        self.destination_folder = destination_folder
        self.module = None
        self.load_script()

    def load_script(self):
        spec = importlib.util.spec_from_file_location("script_module", self.script_path)
        self.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.module)

    def on_created(self, event):
        print(f"File created: {event.src_path}")

        if (not event.is_directory and
            not os.path.basename(event.src_path).startswith('.') and
            not event.src_path.endswith('.crdownload') and
            not event.src_path.endswith('.part') and
            os.path.basename(event.src_path).startswith(self.pattern)):

            print(f"New file detected: {event.src_path}")

            time.sleep(5)

            if os.path.exists(event.src_path) and not self.is_file_being_written(event.src_path):
                print(f"Processing file: {event.src_path}")
                self.move_file(event.src_path)
                self.run_script()

    def is_file_being_written(self, filepath):
        initial_size = os.path.getsize(filepath)
        time.sleep(1)
        final_size = os.path.getsize(filepath)
        return initial_size != final_size

    def move_file(self, filepath):
        try:
            os.makedirs(self.destination_folder, exist_ok=True)
            shutil.move(filepath, os.path.join(self.destination_folder, os.path.basename(filepath)))
            print(f"File moved to: {self.destination_folder}")
        except Exception as e:
            print(f"Failed to move file: {e}")

    def run_script(self):
        func = getattr(self.module, self.function_name)
        func()

def monitor_folder(folder_path, pattern, script_path, function_name, destination_folder):
    event_handler = DownloadEventHandler(pattern, script_path, function_name, destination_folder)
    observer = Observer()
    observer.schedule(event_handler, path=folder_path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    downloads_folder = os.path.expanduser("~/Downloads")
    filename_pattern = "poker_now_log_"
    script_path = os.path.join(os.path.dirname(__file__), "pokernow_to_pokertracker.py")
    function_name = "pokernow_to_pokertracker"
    destination_folder = os.path.expanduser("~/Documents/Personal/Poker/Poker Script/pokernow_logs")

    monitor_folder(downloads_folder, filename_pattern, script_path, function_name, destination_folder)
