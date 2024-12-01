# Write your solution here
_number1: int = int(input("Number 1: "))
_number2: int = int(input("Number 2: "))
_operation: str = input("Operation: ")

if _operation == "add":
    print(f"{_number1} + {_number2} = {_number1 + _number2}")
elif _operation == "multiply":
    print(f"{_number1} * {_number2} = {_number1 * _number2}")
elif _operation == "subtract":
    print(f"{_number1} - {_number2} = {_number1 - _number2}")