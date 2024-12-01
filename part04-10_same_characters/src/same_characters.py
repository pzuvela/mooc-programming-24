# Write your solution here
def same_chars(word: str, ind1: int, ind2: int) -> bool:
    if ind1 >= len(word) or ind2 >= len(word):
        return False
    return word[ind1] == word[ind2]

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))
    print(same_chars("abc", 0, 3))
