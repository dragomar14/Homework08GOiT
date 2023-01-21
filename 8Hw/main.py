from datetime import datetime, timedelta
import calendar
from collections import defaultdict

weekdays = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}
users1 = [
    {"Mike": "2000-01-22"},
    {"Bob": "2002-01-25"},
    {"Tom": "2001-01-23"},
    {"Smith": "1995-01-24"},
    {"Dwayne": "1998-01-27"},
    {"Jim": "2005-04-02"},
    {"Oscar": "2003-04-04"}
        ]
def get_birthdays_per_week(users, per=7):
    result = defaultdict(list)
    current_datetime = datetime.now()
    current_date_only = current_datetime.date()
    end = current_date_only + timedelta(days=per)
    current_date_for_delta = datetime(year=current_datetime.year, month=current_datetime.month, day=current_datetime.day)
    for open_list in users:
        for name, birthday in open_list.items():
            birthday_date = datetime.strptime(birthday, "%Y-%m-%d")
            birthday_date_for_delta = datetime(year=current_datetime.year, month=birthday_date.month, day=birthday_date.day)
            if current_date_for_delta.date() <= birthday_date_for_delta.date() < end:
                work_days = birthday_date_for_delta.weekday()
                if work_days not in (5, 6):
                    result[birthday_date_for_delta].append(name)
                elif work_days == 5:
                    result[birthday_date_for_delta+timedelta(days=2)].append(name)
                elif work_days == 6:
                    result[birthday_date_for_delta + timedelta(days=1)].append(name)
            else:
                continue
    if len(result) == 0:
        print("Nobody have a birthday in this range")
    else:
        for f in sorted(result):
            res1 = ", ".join(result[f])
            print(f"{weekdays[f.weekday()]}: {res1}")



if __name__ == "__main__":
    get_birthdays_per_week(users1)