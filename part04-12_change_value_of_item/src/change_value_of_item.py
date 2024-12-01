# Write your solution here
list_ = [1, 2, 3, 4, 5]

while True:

    index: int = int(input("Index: "))

    if index == -1:
        break

    new_value: int = int(input("New value: "))

    list_[index] = new_value

    print(list_)
