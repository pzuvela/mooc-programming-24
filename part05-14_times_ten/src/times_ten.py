# Write your solution here
def times_ten(start_index: int, end_index: int) -> dict[int, int]:
    return {number: number * 10 for number in range(start_index, end_index + 1)}


if __name__ == "__main__":
    print(times_ten(3, 6))
