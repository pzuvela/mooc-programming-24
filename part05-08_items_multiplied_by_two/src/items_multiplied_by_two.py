# Write your solution here
def double_items(numbers: list) -> list:
    return [number * 2 for number in numbers]


if __name__ == "__main__":
    numbers_ = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers_)
    print("original:", numbers_)
    print("doubled:", numbers_doubled)
