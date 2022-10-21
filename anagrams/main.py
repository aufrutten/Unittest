__author__ = 'Semykopenko Ihor'
__version__ = 4
__status_of_task__ = 'Done'

__all__ = ['text_reverse', 'reverse_word', 'reverse_word_with_rules', 'alphabet', 'numbers', 'symbols']

numbers = '0123456789'
symbols = '§±!@#$%^&*()-=_+[]{}\'"\\:;,./<>?'
rules = numbers + symbols
alphabet = [chr(letter) for letter in range(97, 123)] + [chr(letter) for letter in range(65, 91)]


def check_in_the_rules(word: str) -> bool: return any(char for char in word if char in rules)


def reverse_word_with_rules(word: str) -> list:
    """function for reversing word with rules"""
    result = []
    zip_symbols = {index: char for index, char in enumerate(word) if char in rules}
    cleared_word = [char for char in word if char in alphabet]  # cleared text which found in alphabets
    for index, letter in enumerate(word):
        if index in zip_symbols:
            result.append(letter)
        else:
            result.append(cleared_word.pop())
    return result


def reverse_word(word: str) -> str:
    """this function return word in reverse in the selected rules"""
    assert type(word) == str, "you wrote wrong type of arg, allowable: str"
    #  if the word have anything number or symbol
    if check_in_the_rules(word):
        return ''.join(reverse_word_with_rules(word))
    else:  # if the word doesn't haА у а уve anything number or symbol
        return ''.join(list(word)[::-1])


def text_reverse(string: str) -> str:
    """
    function for reverse text and which leaves symbols and numbers in their place
    :return str, function always return string, not depended on argument
    """
    assert type(string) is str or type(string) is float or type(string) is int,\
        "you wrote wrong type of arg, allowable: str, int, float"

    # getting list of word, with separator " " - space | exp: 'hello world' -> ['hello', 'world']
    if type(string) == str:
        return ' '.join([reverse_word(word) for word in string.split(' ')])
    elif type(string) == int or type(string) == float:
        return ' '.join([reverse_word(word) for word in str(string).split(' ')])

