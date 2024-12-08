# Write your solution here
def get_prefixes():
    return ["thir", "four", "fif", "six", "seven", "eigh", "nine"]


def get_single_digit_numbers_words():
    return [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"
    ]


def get_double_digit_words() -> list[str]:

    prefixes = get_prefixes()
    single_digit_numbers_words = get_single_digit_numbers_words()

    words = [
        "eleven", "twelve"
    ]

    for prefix in prefixes:
        words += [f"{prefix}teen"]

    for prefix in ["twen"] + prefixes:
        if prefix == "four":
            prefix = "for"
        words += [f"{prefix}ty"]
        words += [f"{prefix}ty-{word}" for word in single_digit_numbers_words[1:-1]]

    return words


def dict_of_numbers():
    numbers = range(100)
    words = [*get_single_digit_numbers_words(), *get_double_digit_words(),]

    return {number: word for number, word in zip(numbers, words)}


if __name__ == "__main__":
    """
    Please write a function named dict_of_numbers(), which returns a new dictionary. 
    The dictionary should have the numbers from 0 to 99 as its keys. 
    The value attached to each key should be the number spelled out in words. 
    Please have a look at the example below
    """
    numbers_ = dict_of_numbers()
    print(numbers_[2])
    print(numbers_[11])
    print(numbers_[45])
    print(numbers_[99])
    print(numbers_[0])
