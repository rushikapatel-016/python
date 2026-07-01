from datetime import date

today = date.today()

print("Today is", today.strftime("%A, %d %B %Y"))

new_year = date(2027, 1, 1)

days_left = new_year - today

print("Days left until 1st January 2027:", days_left.days)