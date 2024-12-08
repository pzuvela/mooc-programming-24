# Write your solution here
def factorial(number):
    if number == 0:
        return 1
    return factorial(number - 1) * number


def factorials(n: int) -> dict[int, int]:
    return {number: factorial(number) for number in range(1, n + 1)}


if __name__ == "__main__":
    print(factorials(10))
