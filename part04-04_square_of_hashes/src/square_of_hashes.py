# Copy here code of line function from previous exercise
def line(length: int, x: str):
    print(x * length)

def square_of_hashes(size):
    # You should call function line here with proper parameters
    for _ in range(size):
        line(size, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
