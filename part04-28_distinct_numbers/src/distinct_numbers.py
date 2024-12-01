# Write your solution here

def distinct_numbers(lst):
    
    lst.sort()
    distinct_lst = []
    
    for i in lst:
        if i not in distinct_lst:
            distinct_lst.append(i)
    
    return distinct_lst


if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]
