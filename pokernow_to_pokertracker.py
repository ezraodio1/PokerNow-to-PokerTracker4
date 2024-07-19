import os
from my_utils import process_file, upload_to_PT4, move_files

def pokernow_to_pokertracker():
    source_folder = 'pokernow_logs'
    destination_folder = 'old_pokernow_logs'

    os.makedirs(destination_folder, exist_ok=True)

    shouldUpload = False
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        if os.path.isfile(file_path):
            success = process_file(filename)
            if success:
                new_file_path = os.path.join(destination_folder, filename)
                os.rename(file_path, new_file_path)
                print(f"Moved {filename} to {destination_folder}")
                shouldUpload = True
            else:
                print(f"Did not move {filename} due to processing failure")

    if shouldUpload:
        uploaded = upload_to_PT4()
        if uploaded:
            move_files('pokerstars_format_logs', 'uploaded_logs')