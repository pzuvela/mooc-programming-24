# Write your solution here
def histogram(s: str) -> None:
    unique_s = set(s)
    histogram_dict: dict[str, int] = {s_: s.count(s_) for s_ in unique_s}
    for key, val in histogram_dict.items():
        print(f"{key} {'*' * val}")


if __name__ == "__main__":
    print(histogram("statistically"))
