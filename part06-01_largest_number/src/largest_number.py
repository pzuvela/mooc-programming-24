# write your solution here
import os

def largest():
    with open(os.path.join(os.path.dirname(__file__), "numbers.txt"), "r") as f:
        numbers = f.readlines()
    return int(max(numbers, key=lambda x: int(x)))


if __name__ == "__main__":
    print(largest())
