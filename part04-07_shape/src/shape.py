# Copy here code of line function from previous exercise and use it in your solution
def line(size: int, character: str):
    print(size * character)

def shape(size1: int, character1: str, size2: int, character2: str):
    for i in range(size1):
        line(i+1, character1)
    for _ in range(size2):
        line(size1, character2)


# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")
