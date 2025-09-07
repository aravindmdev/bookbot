import sys
from stats import get_word_count, get_char_count, get_sorted_char_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    file_contents = get_book_text(file_path)
    word_count = get_word_count(file_contents)
    char_counts = get_char_count(file_contents)
    char_count_sorted = get_sorted_char_list(char_counts)

    # print(f"{word_count} words found in the document")
    # # print(char_counts)
    # print(char_count_sorted)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for item in char_count_sorted:
        print(f"{item["char"]}: {item["num"]}")

main()