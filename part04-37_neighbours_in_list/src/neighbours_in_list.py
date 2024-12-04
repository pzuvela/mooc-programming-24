# Write your solution here

def longest_series_of_neighbours(lst) -> int:
    
    neighbours_series_lengths = []
    neighbours_series_length = 0
    
    for i in range(len(lst)-1):
        
        if abs(lst[i+1] - lst[i]) == 1:
            neighbours_series_length += 1
        else:
            neighbours_series_lengths.append(neighbours_series_length + 1)
            neighbours_series_length = 0
        if i == (len(lst) - 1)-1:
            neighbours_series_lengths.append(neighbours_series_length + 1)
    
    return max(neighbours_series_lengths)


if __name__ == "__main__":

    my_list = [5, 3, 4, 2, 3, 1, 2, 3, 9, 8, 7, 8, 7, 6, 7, 6]
    print(longest_series_of_neighbours(my_list))

    # my_list = [1, 2]
    # print(longest_series_of_neighbours(my_list))

    # my_list = [1, 2, 3, 5, 6, 9, 10]
    # print(longest_series_of_neighbours(my_list))
