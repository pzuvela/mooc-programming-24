# Write your solution here
def invert(d: dict):
    inverted_d = {val: key for key, val in d.items()}
    d.clear()
    for key, val in inverted_d.items():
        d[key] = val


if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    print(s)
    invert(s)
    print(s)
