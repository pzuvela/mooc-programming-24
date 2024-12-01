# Write your solution here
def length_of_longest(lst) -> int:
    max_length: int = len(max(lst, key=lambda x: len(x)))
    return max_length


if __name__ == "__main__":

    my_list = ["first", "second", "fourth", "eleventh"]

    result = length_of_longest(my_list)
    print(result)
