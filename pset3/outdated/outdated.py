import re

months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

while True:
    date = input("Date: ")
    try:
        month, day, year = date.split('/')
        month, day, year = int(month), int(day), int(year)
    except ValueError:
        pass
    else:
        if 0 < day <= 31 and 0 < month <= 12:
            print(f"{year}-{month:02d}-{day:02d}")
            break
    try:
        month, day, year = re.split(' |, ', date)
        day = int(day)
        month = int(months[month])
    except (ValueError, KeyError):
        pass
    else:
        if 0 < day <= 31 and ',' in date:
            print(f"{year}-{month:02d}-{day:02d}")
            break