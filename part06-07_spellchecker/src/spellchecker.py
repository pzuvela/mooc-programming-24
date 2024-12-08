# write your solution here
import os

def get_word_list() -> list[str]:
    with open(os.path.join(os.path.dirname(__file__), "wordlist.txt"), "r") as f:
        return [line.strip() for line in f]

word_list: list[str] = get_word_list()

def spell_check(text: list[str]):
    return " ".join(
        [word if word.lower() in word_list else f"*{word}*" for word in text]
    )


text_: str = input("Write text: ")

print(spell_check(text_.split()))
