from datetime import datetime, timedelta

def display_current_datetime():
    """Displays the current date and time."""
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date(days_to_add):
    """Calculates the future date after adding specified days to the current date."""
    future_date = datetime.now() + timedelta(days=days_to_add)
    formatted_future = future_date.strftime("%Y-%m-%d")
    return formatted_future

# Main Program
display_current_datetime()
days_to_add = int(input("Enter the number of days to add to the current date: "))
print(f"Future date: {calculate_future_date(days_to_add)}")
