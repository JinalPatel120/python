from datetime import datetime


def convert_timestamps_to_dates(timestamps):
    return [datetime.fromtimestamp(ts / 1000).strftime('%Y-%m-%d') for ts in timestamps]

# Example usage
timestamps = [
    1698019200000,
    1698192000000,
    1698278400000,
    1698364800000
]
dates = convert_timestamps_to_dates(timestamps)
print(dates)
