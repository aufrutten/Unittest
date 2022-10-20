
import unittest
import anagrams

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


class TestAnagrams(unittest.TestCase):

    def test_of_text_reverse(self) -> None:
        for input_text, output_text in typical_behavior:
            self.assertEqual(anagrams.text_reverse(input_text), output_text, msg=f'text_reverse: {input_text}')

    def test_of_reverse_word(self):
        self.assertEqual(anagrams.reverse_word('pyth123@on'), 'noht123@yp', msg='reverse_word: "pyth123@on"')

    def test_of_reverse_word_with_rules(self):
        self.assertEqual(anagrams.reverse_word_with_rules("x!x"), ['x', '!', 'x'])


if __name__ == '__main__':
    unittest.main()
