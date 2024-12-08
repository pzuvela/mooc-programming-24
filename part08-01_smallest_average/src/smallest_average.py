# Write your solution here
def smallest_average(*args):
    """
    args: person1: dict, person2: dict, person3: dict
    """
    return min(*args, key=lambda x: (x["result1"] + x["result2"] + x["result3"]) / 3)


if __name__ == "__main__":

    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

    print(smallest_average(person1, person2, person3))
