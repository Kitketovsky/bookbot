import re
import sys
    
from stats import get_num_words

def count_symbols(text):
    result = {}

    for char in text.lower():
        if char not in result:
            result[char] = 0

        result[char] += 1

    return result

def printLettersReport(chars_count_dict):
    regex = "[a-zA-Z]"

    for char in chars_count_dict:
        if re.search(regex, char) != None:
            print(f"{char}: {chars_count_dict[char]}")

    return None

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 

    path_to_file = sys.argv[1]

    with open(path_to_file) as f:
        file_contents = f.read()

        print(f"--- Begin report of {path_to_file} ---")

        get_num_words(file_contents)

        chars_count_dict = count_symbols(file_contents)
        printLettersReport(chars_count_dict)

        print("--- End report ---")

main()
