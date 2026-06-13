from string import ascii_uppercase
import re

LETTERS = ascii_uppercase


def get_word_pattern(word):
    letter_nums = {}
    next_num = 0
    pattern = []

    for letter in word.upper():

        if letter not in letter_nums:
            letter_nums[letter] = str(next_num)
            next_num += 1

        pattern.append(letter_nums[letter])

    return ".".join(pattern)
def build_pattern_dictionary(words):
    pattern_dict = {}

    for word in words:
        pattern = get_word_pattern(word)

        if pattern not in pattern_dict:
            pattern_dict[pattern] = []

        pattern_dict[pattern].append(word.upper())

    return pattern_dict


def main():

    words = ["HELLO", "JELLY", "WORLD", "APPLE", "LEVEL"]

    pattern_dict = build_pattern_dictionary(words)

    print(pattern_dict)

if __name__ == "__main__":
    main()

