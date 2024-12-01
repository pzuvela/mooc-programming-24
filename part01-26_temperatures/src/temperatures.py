# Write your solution here
_temperature: int = int(input("Please type in temperature (F): "))

_temperature_in_c: float = (_temperature - 32) * (5/9)

print(f"{_temperature} degrees Fahrenheit equals {_temperature_in_c} degrees Celsius")

if _temperature_in_c < 0:
    print("Brr! It's cold in here!")
