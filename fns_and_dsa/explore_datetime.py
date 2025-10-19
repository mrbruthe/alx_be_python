import datetime

def display_current_datetime():
    """Displays the current date and time."""
current_date = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
print(f"Current date and time is {current_date}")
