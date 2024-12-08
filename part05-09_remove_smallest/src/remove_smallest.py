# Write your solution here
def remove_smallest(numbers: list):
    numbers.remove(min(numbers))


if __name__ == "__main__":
    numbers_ = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers_)
    print(numbers_)
