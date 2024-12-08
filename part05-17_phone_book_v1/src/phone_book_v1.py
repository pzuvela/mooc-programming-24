# Write your solution here

phone_book: dict[str, str] = {}

while True:
    
    command: int = int(input("command (1 search, 2 add, 3 quit): "))

    if command == 2:
        name = input("name: ")
        number = input("number: ")
        phone_book[name] = number
        print("ok!")
    elif command == 1:
        name = input("name: ")        
        print(phone_book.get(name, "no number"))
    elif command == 3:
        print("quitting...")
        break
    else:
        print("Invalid option selected!")
