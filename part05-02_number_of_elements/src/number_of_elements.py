# Write your solution here
def count_matching_elements(my_matrix: list[list[int]], element: int) -> int:
    return sum(row.count(element) for row in my_matrix)


if __name__ == "__main__":
    """
    Please write a function named count_matching_elements(my_matrix: list, element: int), 
    which takes a two-dimensional array of integers and a single integer value as its arguments. 
    The function then counts how many elements within the matrix match the argument value.
    """
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))
