def add_time(start, duration, day=""):
    """
    Adds a duration to a start time and optionally returns the new day.
    Prints the final time in 12-hour format with AM/PM.
    """
    # Convert start time to 24-hour format
    start_parts = start.split()
    time_part, period = start_parts[0], start_parts[1]
    start_hour, start_minute = map(int, time_part.split(":"))

    if period == "PM" and start_hour != 12:
        start_hour += 12
    elif period == "AM" and start_hour == 12:
        start_hour = 0

    # Parse duration
    duration_hour, duration_minute = map(int, duration.split(":"))

    # Calculate new time
    total_minutes = start_minute + duration_minute
    extra_hours = total_minutes // 60
    total_minutes %= 60

    total_hours = start_hour + duration_hour + extra_hours
    days_later = total_hours // 24
    total_hours %= 24

    # Convert back to 12-hour format
    if total_hours == 0:
        display_hour = 12
        period = "AM"
    elif total_hours < 12:
        display_hour = total_hours
        period = "AM"
    elif total_hours == 12:
        display_hour = 12
        period = "PM"
    else:
        display_hour = total_hours - 12
        period = "PM"

    # Handle optional day of the week
    day_str = ""
    if day:
        new_day = find_day(day, days_later)
        day_str = f", {new_day}"

    # Handle days later message
    if days_later == 1:
        days_later_str = " (next day)"
    elif days_later > 1:
        days_later_str = f" ({days_later} days later)"
    else:
        days_later_str = ""

    final_time = f"{display_hour}:{total_minutes:02d} {period}{day_str}{days_later_str}"
    print(final_time)


def find_day(day, days_later):
    """
    Returns the day of the week after adding days_later to the given day.
    """
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    index = days.index(day.capitalize())
    new_index = (index + days_later) % 7
    return days[new_index]


add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
