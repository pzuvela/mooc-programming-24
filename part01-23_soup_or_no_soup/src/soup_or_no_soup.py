# Write your solution here
_name: str = input("Please tell me your name: ")

if _name != "Jerry":
    _portion_price: float = 5.90
    _n_portions: int = int(input("How many portions of soup? "))
    print(f"The total cost is {_n_portions * _portion_price}")
print("Next please!")

