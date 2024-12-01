# Write your solution here
def shortest(lst) -> str:
    min_: str = min(lst, key=lambda x: len(x))
    return min_


if __name__ == "__main__":

    my_list = ["first", "second", "fourth", "eleventh"]

    result = shortest(my_list)
    print(result)
