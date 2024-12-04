# Write your solution here
def no_vowels(s: str) -> str:
    return "".join([s_ for s_ in s if s_ not in {"a", "e", "i", "o", "u"}])


if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))
