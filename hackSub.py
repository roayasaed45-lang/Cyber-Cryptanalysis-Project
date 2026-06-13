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


def main():

    print(get_word_pattern("HELLO"))
    print(get_word_pattern("JELLY"))
    print(get_word_pattern("WORLD"))


if __name__ == "__main__":
    main()
