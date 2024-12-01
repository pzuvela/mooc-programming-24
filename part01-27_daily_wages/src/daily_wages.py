# Write your solution here
_hourly_wage: float = float(input("Hourly wage: "))
_hours_worked: int = int(input("Hours worked: "))
_day_of_the_week: str = input("Day of the week: ")

_daily_wages: float = _hourly_wage * _hours_worked

if _day_of_the_week == "Sunday":
    _daily_wages *= 2

print(f"Daily wages: {_daily_wages} euros")