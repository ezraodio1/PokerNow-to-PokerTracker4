from poker_now_log_converter.main import convert_poker_now_files
import os
import shutil
import subprocess
import time
from AppKit import NSWorkspace
from Quartz.CoreGraphics import (
    CGEventCreateMouseEvent, CGEventCreateKeyboardEvent, CGEventPost,
    kCGEventLeftMouseDown, kCGEventLeftMouseUp, kCGEventMouseMoved,
    kCGMouseButtonLeft, CGPoint
)


def process_file(filename):
    if filename in os.listdir('old_pokernow_logs'):
        print(f"File {filename} has already been converted")
        return False
    try:
        file_path = 'pokernow_logs/' + filename
        print(f"Processing {filename}")
        convert_poker_now_files(hero_name="ezra", input_filename=file_path, output_directory='pokerstars_format_logs')
        return True
    except Exception as e:
        print(f"Failed to process {filename}: {e}")
        return False

def upload_to_PT4():
    PT4_PATH = '/Applications/PokerTracker 4.app'
    NSWorkspace.sharedWorkspace().launchApplication_(PT4_PATH)
    time.sleep(5)
    click_ok_button()
    time.sleep(5)
    enter_full_screen()
    time.sleep(1)
    click_play_poker()
    time.sleep(1)
    click_get_hands_from_disk()
    time.sleep(1)
    click_select_files()
    time.sleep(1)
    navigate_and_select_in_dialog('~/Documents/Personal/Poker/Poker Script/pokerstars_format_logs')
    time.sleep(1)
    click_first_file()
    time.sleep(5)
    click_open()
    time.sleep(1)
    click_confirm_import()
    time.sleep(1)
    return True

def click_first_file():
    click_mouse(466, 270)

def click_open():
    click_mouse(1205, 637)

def navigate_and_select_in_dialog(folder_path):
    script = f"""
    tell application "System Events"
        tell process "PokerTracker 4"
            set frontmost to true
            delay 1
            keystroke "G" using {{command down, shift down}}
            delay 1
            keystroke "{folder_path}"
            delay 1
            keystroke return
        end tell
    end tell
    """
    subprocess.run(['osascript', '-e', script])

def click_confirm_import():
    click_mouse(853, 597)

def click_select_files():
    click_mouse(714, 595)

def click_get_hands_from_disk():
    click_mouse(537, 118)

def click_select_directory():
    click_mouse(831, 596)

def click_play_poker():
    click_mouse(122, 80)

def enter_full_screen():
    key_cmd_down = CGEventCreateKeyboardEvent(None, 0x37, True)
    key_ctrl_down = CGEventCreateKeyboardEvent(None, 0x3b, True)
    key_f_down = CGEventCreateKeyboardEvent(None, 0x03, True)

    key_f_up = CGEventCreateKeyboardEvent(None, 0x03, False)
    key_ctrl_up = CGEventCreateKeyboardEvent(None, 0x3b, False)
    key_cmd_up = CGEventCreateKeyboardEvent(None, 0x37, False)

    CGEventPost(0, key_cmd_down)
    CGEventPost(0, key_ctrl_down)
    CGEventPost(0, key_f_down)

    CGEventPost(0, key_f_up)
    CGEventPost(0, key_ctrl_up)
    CGEventPost(0, key_cmd_up)

def click_ok_button():
    click_mouse(941, 696)

def move_mouse_to(x, y):
    event = CGEventCreateMouseEvent(None, kCGEventMouseMoved, CGPoint(x, y), kCGMouseButtonLeft)
    CGEventPost(0, event)

def click_mouse(x, y):
    move_mouse_to(x, y)
    event_down = CGEventCreateMouseEvent(None, kCGEventLeftMouseDown, CGPoint(x, y), kCGMouseButtonLeft)
    event_up = CGEventCreateMouseEvent(None, kCGEventLeftMouseUp, CGPoint(x, y), kCGMouseButtonLeft)
    CGEventPost(0, event_down)
    CGEventPost(0, event_up)

def move_files(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for filename in os.listdir(source_folder):
        source_file = os.path.join(source_folder, filename)
        destination_file = os.path.join(destination_folder, filename)

        if os.path.isfile(source_file):
            shutil.move(source_file, destination_file)
            print(f"Moved {source_file} to {destination_file}")
