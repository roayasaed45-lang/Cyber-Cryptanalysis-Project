# Substitution Cipher Cracker

## Overview

This project implements a dictionary-based cryptanalysis attack against a Simple Substitution Cipher.

The program attempts to recover the original plaintext without knowing the encryption key by analyzing word patterns, searching a dictionary for matching candidates, building possible letter mappings, reducing conflicts, and decrypting the ciphertext.

This project was developed as part of a Cyber Security and Cryptography course.

---

# Project Architecture

The system is divided into several logical stages:

```text
Cipher Text
     │
     ▼
Split Into Words
     │
     ▼
Generate Word Patterns
     │
     ▼
Dictionary Pattern Matching
     │
     ▼
Build Candidate Mappings
     │
     ▼
Constraint Reduction
     │
     ▼
Decrypt Ciphertext
```

---

# Project Structure

```text
Substitution-Cipher-Cracker/
│
├── hackSub.py
├── README.md
```

---

# Algorithm Stages

## Stage 1 – Split Cipher Text

The encrypted message is divided into individual words.

Example:

```text
Sy l nlx sr pyyacao
```

↓

```python
['Sy', 'l', 'nlx', 'sr', 'pyyacao']
```

---

## Stage 2 – Generate Word Patterns

Each word is converted into a structural pattern based on repeated letters.

Examples:

```text
HELLO  -> 0.1.2.2.3
JELLY  -> 0.1.2.2.3
WORLD  -> 0.1.2.3.4
```

Words with the same pattern are considered possible matches.

---

## Stage 3 – Dictionary Pattern Matching

For each encrypted word, the system searches the dictionary for words with the same pattern.

Example:

```text
pyyacao -> OFFERED
```

---

## Stage 4 – Build Candidate Mappings

Possible mappings between encrypted and plaintext letters are generated.

Example:

```text
P -> O
Y -> F
A -> E
C -> R
O -> D
```

---

## Stage 5 – Constraint Reduction

The algorithm removes conflicting possibilities.

If:

```text
C -> R
```

is already confirmed, then the letter:

```text
R
```

cannot appear as a possibility for any other encrypted letter.

This process is repeated until no further reductions can be made.

---

## Stage 6 – Decrypt Cipher Text

The final mapping is used to decrypt the entire message.

Unknown letters are displayed as:

```text
_
```

until enough information is available.

---

# Example Result

Encrypted text:

```text
Sy l nlx sr pyyacao l ylwj eiswi...
```

Decrypted text:

```text
If a man is offered a fact which goes against his instincts...
```

---

# Main Functions

| Function                   | Purpose                                       |
| -------------------------- | --------------------------------------------- |
| get_word_pattern()         | Generates a pattern for a word                |
| build_pattern_dictionary() | Creates dictionary indexed by patterns        |
| get_blank_mapping()        | Creates an empty mapping table                |
| add_letters_to_mapping()   | Adds candidate letter mappings                |
| reduce_mapping()           | Removes conflicting mappings                  |
| decrypt_with_mapping()     | Decrypts ciphertext using discovered mappings |
| main()                     | Executes the attack process                   |

---

# Technologies Used

* Python 3
* Dictionary Attack
* Pattern Matching
* Constraint Reduction
* Cryptanalysis Techniques

---

# Author

Roaya Saed

B.Sc. Information Systems (MIS)

Cyber Security & Cryptography Course
