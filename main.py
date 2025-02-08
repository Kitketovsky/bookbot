import re

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
            print(f"The '{char}' character was found {chars_count_dict[char]} times")

    return None

def main(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

        print(f"--- Begin report of {path_to_file} ---")

        words_count = len(file_contents.split())

        print(f"{words_count} words found in the document")
        print("\n")

        chars_count_dict = count_symbols(file_contents)
        printLettersReport(chars_count_dict)

        print("--- End report ---")

main("books/frankenstein.txt")