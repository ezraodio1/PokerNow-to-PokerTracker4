# Poker Now Log Converter

A script to monitor your Downloads folder for PokerNow log files, convert them, and upload the converted logs to PokerTracker4.

## Overview

This project is designed to automate the process of converting PokerNow log files and uploading them to PokerTracker4. It monitors your Downloads folder for new PokerNow log files, converts the files into a format compatible with PokerTracker4, and uploads them automatically.

## Features

- **Automatic Monitoring**: Continuously monitors the Downloads folder for new PokerNow log files.
- **Conversion**: Converts PokerNow log files into a format compatible with PokerTracker4.
- **Automation**: Automatically uploads the converted log files to PokerTracker4.

## Requirements

- Dependencies listed in `requirements.txt`

## Instructions

- Activate venv with `python -m venv venv` then `source venv/bin/activate`
- Install dependencies with `pip install -r requirements.txt`
- Run `python main.py` to start monitoring downloads file