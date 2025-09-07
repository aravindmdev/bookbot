def get_word_count(file_contents):
    words = file_contents.split()
    return len(words)

def get_char_count(file_contents):
    char_counts = {}

    for char in file_contents:
        char = char.lower()
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts

def sort_on(items):
    return items["num"]

def get_sorted_char_list(char_counts):
    char_count_list = []

    for char in char_counts:
        if char.isalpha():
            char_count_list.append({"char": char, "num": char_counts[char]})

    char_count_list.sort(reverse=True, key=sort_on)

    return char_count_list