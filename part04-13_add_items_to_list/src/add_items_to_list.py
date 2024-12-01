# Write your solution here

n_items: int = int(input("How many items: "))

items = []

for n in range(n_items):
    items.append(int(input(f"Item {n+1}: ")))

print(items)
