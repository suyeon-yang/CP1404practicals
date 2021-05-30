"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(string, n):
    """Repeat string s, n times, with spaces in between."""
    my_str = ' '.join([string]*n)
    return my_str


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"

    test_car = Car(fuel=10)
    assert test_car.fuel == 10


run_tests()


def phrase_to_sentence(phrase):
    """
    >>> phrase_to_sentence("hello world")
    'Hello world.'
    >>> phrase_to_sentence("you are pretty")
    'You are pretty.'
    >>> phrase_to_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> phrase_to_sentence("hello")
    'Hello.'
    """

    sentence = phrase.capitalize()
    if sentence[-1] != ".":
        sentence += "."
    return sentence


doctest.testmod()
