from string import ascii_uppercase
import re

LETTERS = ascii_uppercase


def get_word_pattern(word):
    word = re.sub(r"[^A-Za-z]", "", word)
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

def get_candidate_mapping(cipher_word, candidate_word):
    mapping = {}

    cipher_word = cipher_word.upper()
    candidate_word = candidate_word.upper()

    for i in range(len(cipher_word)):
        cipher_letter = cipher_word[i]
        plain_letter = candidate_word[i]

        mapping[cipher_letter] = plain_letter

    return mapping

def get_blank_mapping():
    mapping = {}

    for letter in LETTERS:
        mapping[letter] = []

    return mapping

def add_letters_to_mapping(mapping, cipher_word, candidate_word):
    cipher_word = re.sub(r"[^A-Za-z]", "", cipher_word).upper()
    candidate_word = re.sub(r"[^A-Za-z]", "", candidate_word).upper()

    for i in range(len(cipher_word)):
        cipher_letter = cipher_word[i]
        plain_letter = candidate_word[i]

        if plain_letter not in mapping[cipher_letter]:
            mapping[cipher_letter].append(plain_letter)

    return mapping

def reduce_mapping(mapping):
    changed = True

    while changed:
        changed = False

        solved_letters = []

        for cipher_letter in mapping:
            if len(mapping[cipher_letter]) == 1:
                solved_letters.append(mapping[cipher_letter][0])

        for cipher_letter in mapping:
            if len(mapping[cipher_letter]) > 1:
                before = mapping[cipher_letter].copy()

                for solved in solved_letters:
                    if solved in mapping[cipher_letter]:
                        mapping[cipher_letter].remove(solved)

                if before != mapping[cipher_letter]:
                    changed = True

    return mapping


def decrypt_with_mapping(cipher_text, mapping):
    result = ""

    for symbol in cipher_text:
        upper_symbol = symbol.upper()

        if upper_symbol in LETTERS:
            possible_letters = mapping[upper_symbol]

            if len(possible_letters) == 1:
                plain_letter = possible_letters[0]
            else:
                plain_letter = "_"

            if symbol.islower():
                result += plain_letter.lower()
            else:
                result += plain_letter
        else:
            result += symbol

    return result

WORDS = [
    "IF", "A", "MAN", "IS", "OFFERED", "FACT", "WHICH", "GOES",
    "AGAINST", "HIS", "INSTINCTS", "HE", "WILL", "SCRUTINIZE",
    "IT", "CLOSELY", "AND", "UNLESS", "THE", "EVIDENCE",
    "OVERWHELMING", "REFUSE", "TO", "BELIEVE", "ON", "OTHER",
    "HAND", "SOMETHING", "AFFORDS", "REASON", "FOR", "ACTING",
    "IN", "ACCORDANCE", "ACCEPT", "EVEN", "SLIGHTEST", "ORIGIN",
    "OF", "MYTHS", "EXPLAINED", "THIS", "WAY", "BERTRAND", "RUSSELL"
]


CIPHER_TEXT = """Sy l nlx sr pyyacao l ylwj eiswi upar lulsxrj isr sxrjsxwjr, 
ia esmm rwctjsxsza sj wmpramh, lxo txmarr jia aqsoaxwa sr pqaceiamnsxu, ia esmm caytra jp famsaqa sj. 
Sy, px jia pjiac ilxo, ia sr pyyacao rpnajisxu eiswi lyypcor l calrpx ypc lwjsxu sx lwwpcolxwa jp isr sxrjsxwjr, 
ia esmm lwwabj sj aqax px jia rmsuijarj aqsoaxwa. Jia pcsusx py nhjir sr agbmlsxao sx jisr elh. -Facjclxo Ctrramm"""


def main():

    pattern_dict = build_pattern_dictionary(WORDS)

    mapping = get_blank_mapping()

    cipher_words = CIPHER_TEXT.split()

    for word in cipher_words:

        pattern = get_word_pattern(word)

        candidates = pattern_dict.get(pattern, [])

        print("\nWord:", word)
        print("Candidates:", candidates)

        if len(candidates) == 1:
            mapping = add_letters_to_mapping(mapping, word, candidates[0])
            mapping = reduce_mapping(mapping)

    decrypted_text = decrypt_with_mapping(CIPHER_TEXT, mapping)

    print("\nFinal Mapping:")
    print(mapping)

    print("\nDecrypted Text:")
    print(decrypted_text)



if __name__ == "__main__":
    main()

