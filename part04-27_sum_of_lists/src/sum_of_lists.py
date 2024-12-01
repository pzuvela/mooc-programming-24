# Write your solution here
# Please write a function named list_sum which takes two lists of integers as arguments. 
# The function returns a new list which contains the sums of the items 
# at each index in the two original lists. 
# You may assume both lists have the same number of items.

def list_sum(lst1, lst2):
    
    lst3 = []

    for i, j in zip(lst1, lst2):
        lst3.append(i + j)

    return lst3


if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]