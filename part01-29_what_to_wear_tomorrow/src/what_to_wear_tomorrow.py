# Write your solution here
_temperature: int = int(input("Temperature: "))
_will_it_rain: str = input("Will it rain (yes/no): ")

print("Wear jeans and a T-shirt")

if _temperature <= 20:
    print("I recommend a jumper as well")

if _temperature <= 10:
    print("Take a jacket with you")

if _temperature <= 5:
    print("Make it a warm coat, actually")
    print("I think gloves are in order")

if _will_it_rain == "yes":
    print("Don't forget your umbrella!")
