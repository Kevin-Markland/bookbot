from stats import *
import sys

def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    rel_path = sys.argv[1]
    book_text = get_book_text(rel_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {rel_path}...")
    print("----------- Word Count ----------")
    word_count(book_text)
    print("--------- Character Count -------")
    sorted_chars = dict_sorter(char_counter(book_text))
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

main()