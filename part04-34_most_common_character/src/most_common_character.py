# Write your solution here

def most_common_character(s: str) -> str:
    return max(s, key=lambda x: s.count(x))


if __name__ == "__main__":

    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))
