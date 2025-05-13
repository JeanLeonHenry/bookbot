from collections import Counter


def get_num_words(s: str) -> int:
    return len(s.split())


def get_num_cars(s: str) -> Counter:
    return Counter(s.lower())
