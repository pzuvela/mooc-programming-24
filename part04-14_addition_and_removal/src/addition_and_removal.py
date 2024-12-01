# Write your solution here
numbers = []

while True:
    print(f"The list is now {numbers}")
    input_ = input("a(d)d, (r)emove or e(x)it ")
    if input_ not in {"d", "r", "x"}:
        print(f"Invalid input: {input_}! Valid inputs {'d', 'r', 'x'}.")
        continue
    if input_ == "d":
        numbers.append(numbers[-1] + 1 if numbers else 1)
    elif input_ == "r":
        if len(numbers) != 0:
            numbers.pop()
        else:
            print("Cannot remove from empty list, add some numbers first!")
            continue
    else:
        print("Bye!")
        break
