# Write your solution here
def longest(lst: list[str]) -> str:
    return max(lst, key=lambda x: len(x))


if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))
