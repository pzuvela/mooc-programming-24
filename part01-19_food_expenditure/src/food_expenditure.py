# Write your solution here

_times_per_week: int = int(input("How many times a week do you eat at the student cafeteria? "))

_price_of_lunch: float = float(input("The price of a typical student lunch? "))
 
_money_for_groceries: float = float(input("How much money do you spend on groceries in a week? "))

_weekly_total: float = _times_per_week * _price_of_lunch + _money_for_groceries

print("Average food expenditure:")
print(f"Daily: {_weekly_total / 7} euros")
print(f"Weekly: {_weekly_total} euros")