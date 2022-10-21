
import unittest
import anagrams
import random

typical_behavior = (
    ("abcd efgh", "dcba hgfe"),
    ("a1bcd efg!h", "d1cba hgf!e"),
    ("", ""),
    ("a1bcd  efg!h", "d1cba  hgf!e"),
    ("   ", "   "),
    ("Hello World!", "olleH dlroW!"),
    ("!Hello World", "!olleH dlroW"),
    ("x!x", "x!x"),
    ("pyth123@on", "noht123@yp"),
    ("ab123", "ba123"),
    ("12312 12312", "12312 12312")
)

atypical_behavior = (
    (123, "123"),
    (3.1415, "3.1415"),
    ([], '3.1415'),
    ({}, "Hello World"),
)


def gen_of_word(len_of_word):

    all_symbols = list(anagrams.symbols) + list(anagrams.numbers) + anagrams.alphabet
    while True:
        password = [all_symbols[random.randint(0, len(all_symbols) - 1)] for _ in range(len_of_word)]
        yield ''.join(password)


def generator_of_text(number_of_cases: int,
                      max_length_of_word: int,
                      max_number_of_words: int,
                      max_number_of_spaces: int):
    result = []
    for _ in range(number_of_cases):  # loop for cases
        text = []

        for _ in range(max_number_of_words):  # loop for words
            gen = gen_of_word(random.randint(1, max_length_of_word))  # create generator
            text.append(next(gen))  # adding text in text
            text.append(' '*random.randint(1, max_number_of_spaces))  # adding spaces in text

        result.append(''.join(text))
    return tuple(result)


class TestAnagrams(unittest.TestCase):

    def test_of_text_reverse(self) -> None:
        """function 'text_reverse' always return string, nothing more"""

        for input_text, output_text in typical_behavior:
            self.assertEqual(anagrams.text_reverse(input_text), output_text, msg=f'text_reverse: {input_text}')

        for input_text, output_text in atypical_behavior:
            try:
                self.assertEqual(anagrams.text_reverse(input_text), output_text, msg=f'text_reverse: {input_text}')
            except AssertionError:
                pass

        for string in generator_of_text(1000, 4, 2, 1):
            double_call_function = anagrams.text_reverse(
                anagrams.text_reverse(string)
            )
            self.assertEqual(double_call_function, string, msg=f'text_reverse: {string}')

    def test_of_reverse_word(self):
        self.assertEqual(anagrams.reverse_word('pyth123@on'), 'noht123@yp', msg='reverse_word: "pyth123@on"')

    def test_of_reverse_word_with_rules(self):
        self.assertEqual(anagrams.reverse_word_with_rules("x!x"), ['x', '!', 'x'])

