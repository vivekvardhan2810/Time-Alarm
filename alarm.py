import time

def set_alarm(minutes=0, seconds=0):
    total_seconds = minutes * 60 + seconds
    if total_seconds > 0:
        print(f"Alarm set for {minutes} minutes and {seconds} seconds.")
        time.sleep(total_seconds)
        print("Time's up! Alarm triggered.")
    else:
        print("Invalid duration. Please provide a valid duration for the alarm.")

# Example: Set alarm for 1 minute and 5 seconds
set_alarm(minutes=1, seconds=5)