# Write your solution here
def all_the_longest(lst) -> str:
    
    max_length = len(max(lst, key=lambda x: len(x)))

    longest = [s for s in lst if len(s) == max_length]

    return longest


if __name__ == "__main__":

    # my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    my_list = ['Paul', 'Ruth', 'Magdalena', 'Jean', 'Larry']
    # my_list = ['Alan', 'Grace', 'Steve', 'Kim', 'Susan']

    result = all_the_longest(my_list)
    print(result)
