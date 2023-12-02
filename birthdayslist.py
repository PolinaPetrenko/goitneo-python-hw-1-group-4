from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    
    weekdays = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }
    birthdays = {day: [] for day in weekdays.values()}  # Створюємо порожні списки для кожного дня тижня

    
    today = datetime.now()

    
    for user in users:
        name = user["name"]
        birthday = user["birthday"]

        
        birthday_this_year = birthday.replace(year=today.year)

        
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

       
        delta_days = (birthday_this_year - today).days

        
        if 0 <= delta_days < 7:
            day_of_week = (today + timedelta(days=delta_days)).weekday()
            weekdays_name = weekdays[day_of_week]
            birthdays[weekdays_name].append(name)

    
    for day, names in birthdays.items():
        if names:
            print(f"{day}: {', '.join(names)}")


users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)},
    {"name": "Natalie Portman", "birthday": datetime(1981, 6, 9)},
    {"name": "Kim Kardashian", "birthday": datetime(1980, 11, 3)},
]    

get_birthdays_per_week(users)


