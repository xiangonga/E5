import time
import os

def focus_timer(work_minutes, break_minutes):
    while True:
        # Work time
        print(f"Work for {work_minutes} minutes.")
        time.sleep(work_minutes * 60)  # Convert minutes to seconds
        os.system("notify-send 'Focus Time Finished' 'Take a Break!'")  # Linux notification
        time.sleep(5)  # Give time to read notification

        # Break time
        print(f"Take a break for {break_minutes} minutes.")
        time.sleep(break_minutes * 60)  # Convert minutes to seconds
        os.system("notify-send 'Break Time Finished' 'Back to Work!'")  # Linux notification
        time.sleep(5)  # Give time to read notification

if __name__ == "__main__":
    work_minutes = 25  # Work time in minutes
    break_minutes = 5  # Break time in minutes
    focus_timer(work_minutes, break_minutes)

import ctypes

def windows_notification(title, message):
    ctypes.windll.user32.MessageBoxW(0, message, title, 0)

# 在需要通知的地方调用
windows_notification('Focus Time Finished', 'Take a Break!')

