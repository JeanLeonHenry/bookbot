from collections import Counter
from operator import itemgetter


def count_words(s: str) -> int:
    return len(s.split())


def count_characters(s: str) -> Counter:
    return Counter(s.lower())


def print_report(s: str) -> None:
    print("--- Report : books/frankenstein.txt ---")
    print(f"{count_words(s)} words found\n")
    for char, count in sorted(
        count_characters(s).items(), key=itemgetter(1), reverse=True
    ):
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")


def main():
    with open("./books/frankenstein.txt", "r") as f:
        file_content = f.read()
    print_report(file_content)


main()
