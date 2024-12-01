# Write your solution here
"""
Please write a program which asks the user to type in values and adds them 
to a list. After each addition, the list is printed out in two different ways:

in the order the items were added ordered from smallest to greatest

The program exits when the user types in 0.

"""

list_ = []

while True:

    new_item = int(input("New item: "))

    if new_item == 0:
        print("Bye!")
        break

    list_.append(new_item)

    print(f"The list now: {list_}")
    # list.sort() sorts the list in place, sorted(list) instantiates a new (sorted) list
    print(f"The list in order: {sorted(list_)}")
