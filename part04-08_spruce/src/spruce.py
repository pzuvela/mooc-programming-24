# Write your solution here
def get_empty_spaces(i: int, total_size: int) -> str:
    return f"{' ' * ((total_size - i) // 2)}"


def spruce(size: int):

    print("a spruce!")
    
    total_size = 2 * size

    for i in range(1, total_size, 2):
        empty_spaces = get_empty_spaces(i, total_size)
        print(f"{empty_spaces}{'*' * i}{empty_spaces}")

    bottom_empty_spaces = get_empty_spaces(1, total_size)
    bottom = f"{bottom_empty_spaces}*{bottom_empty_spaces}"

    print(bottom)


# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(3)
    print()
    spruce(5)
    print()
    spruce(8)
    print()
    spruce(10)
