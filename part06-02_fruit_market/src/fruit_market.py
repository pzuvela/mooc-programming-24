# write your solution here
import os

def read_fruits():
    
    with open(os.path.join(os.path.dirname(__file__), "fruits.csv"), "r") as f:
        fruits = f.readlines()
    
    fruits_ = {}

    for fruit in fruits:
        key, val = fruit.split(";")
        fruits_[key] = float(val)

    return fruits_


if __name__ == "__main__":
    print(read_fruits())
