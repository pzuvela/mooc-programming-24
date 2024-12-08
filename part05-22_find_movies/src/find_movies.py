# Write your solution here
def find_movies(database: list[dict], search_term: str) -> list[dict]:
    results = []
    for entry in database:
        if search_term in entry["name"].lower():
            results.append(entry)
    return results


if __name__ == "__main__":
    database_ = [
        {"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
        {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
        {"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}
    ]

    my_movies = find_movies(database_, "python")
    print(my_movies)
