# Write your solution here
def line(length: int, x: str) -> None:
    
    char = "*"

    if x != "":
        char = x[0]
    
    print(char * length)


# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(3, "")
