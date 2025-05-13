from operator import itemgetter
from stats import get_num_cars, get_num_words
import sys


def print_report(path: str, content: str) -> None:
    def surround(text: str, decoration: str, size: int = 12):
        return f"{decoration * size} {text} {decoration * size}"

    print(surround("BOOKBOT", "="))
    print("Analyzing book found at", path)
    print(surround("Word Count", "-"))
    print(f"Found {get_num_words(content)} total words")
    print(surround("Character Count", "-"))
    for char, count in sorted(
        get_num_cars(content).items(), key=itemgetter(1), reverse=True
    ):
        if char.isalpha():
            print(f"{char}: {count}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    with open(path, "r") as f:
        file_content = f.read()
    print_report(path, file_content)


main()
