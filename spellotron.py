"""
file: spellotron.py
description: Spell checker through various means
language: python3.7
author: Anthony Coneo
"""

import sys

correct_word = dict()
uncorrect_word = []
LEGAL_WORD_FILE = "american-english.txt"
KEY_ADJACENCY_FILE = "keyboard-letters.txt"
GLOBAL_ALPHA = "abcdefghijklmnopqrstuvwxyz"
PUNCTUATIONS = ["_", "-", "[", "]", "{", "}", "(", ")",
                "@", "#", "^", "&", ",", ".", "!", "?",
                ":", ";", "\"", "\'", "*", "+", "=", "/"]


def dict_adjacent(origin_file):
    """
    This function will take the keyboard-letters.txt file and
    create a dictionary key:value pair by taking the first index
    of the file and the rest as the values.
    """
    with open(origin_file) as file:
        dict1 = {}
        for letter in file:
            file = letter.strip().split()
            dict1[file[0]] = file[1:]
        return dict1


def set_adjacent(origin_file):
    """
    This function is suppose to take the words from the
    american-english.txt and have them stored in a set
    for crossword comparison.
    """
    with open(origin_file) as file:
        set_here = set()
        for words in file:
            file = words.strip()
            set_here.add(file)
        return set_here


def key_adjacent(word):
    """
    Purpose: As stated in the project, this functions suppose
    to check in the typed key is incorrect based on user's
    possibility of hitting a key adjacent to the intended one.
    :param word: Inputted words
    :return: checking adjacent keys based on word spelling and
    checking if its correct.
    """
    local_dict = dict_adjacent(KEY_ADJACENCY_FILE)
    local_set = set_adjacent(LEGAL_WORD_FILE)
    for i in range(0, len(word)):
        index_letter = word[i]
        if index_letter in local_dict:
            for value in local_dict[index_letter]:
                created_word = word[0:i] + value + word[i + 1:]
                if created_word in local_set:
                    return created_word
    return word


def missing_letter(word):
    """
    The purpose of this function is to check the inputted word
    and possible missing letters within it by checking the
    GLOBAL_ALPHA.
    """
    local_set = set_adjacent(LEGAL_WORD_FILE)
    for i in range(0, len(word)):
        for phi in GLOBAL_ALPHA:
            new_word = word[:i] + phi + word[i:]
            if new_word in local_set:
                return new_word
    return word


def double_letter(word):
    """
    This function will be used to check if the inputted
    word has a extra letter and it will correct it by
    switching the original word with a new word.
    :param word: Inputted word
    :return: created version of the original word
    """
    local_set = set_adjacent(LEGAL_WORD_FILE)
    for uff in range(0, len(word)):
        new_word = word[:uff] + word[uff+1:]
        if new_word in local_set:
            return new_word
    return word


def capital_correction(word):
    """
    This function will be used to correct the capitalization of
    a given word or line.
    """
    if word[0].upper():
        word_helper = word[0].lower()
        other_word = word_helper + word[1:]
        return other_word
    return word


def word_process(word):
    """
    This function will be used to incorporate all the possible
    issues an inputted word can have. It will check the word and
    take into account what is the issue with it by going through
    the conditionals. After identifying the issues, it will correct
    it by using the functions created above.
    :param word: inputted word or line.
    :return: depends on whats the user_input or file
    """
    cap_correct = capital_correction(word)
    do_letter = double_letter(word)
    miss_letter = missing_letter(word)
    adj_word = key_adjacent(word)
    local_set = set_adjacent(word)

    if word.isdigit():
        return word
    elif adj_word in local_set:
        return adj_word
    elif miss_letter in local_set:
        return miss_letter
    elif do_letter in local_set:
        return do_letter
    elif cap_correct in local_set:
        return cap_correct


def punc_func(word):
    """
    This function is suppose to check against a given word
    for punctuation and letter casing.
    :param word: Inputted word
    """
    lst = []
    for i in word:
        lst.append(i)
    if lst[0] in PUNCTUATIONS:
        lst.pop(0)
    elif lst[-1] in PUNCTUATIONS:
        lst.pop(-1)


def main():
    correct = []
    uncorrect = []
    lst = []
    if len(sys.argv) < 2:
        raise print("python3.7 spellotron.py words/lines (input)")
    elif len(sys.argv) == 2:
        user_input = sys.stdin.readline()
        if sys.argv[1] == "words":
            print(user_input)
        elif sys.argv[1] == "lines":
            print(user_input)
            print(sys.argv[2])
    elif len(sys.argv) == 3:
        user_build = open(sys.argv[2])
        for line in user_build:
            lst.append(line.strip())
            for word in lst:
                return word_process(word)
    elif len(sys.argv) > 3:
        raise print("System Error")

main()