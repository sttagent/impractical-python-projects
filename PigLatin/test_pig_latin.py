import unittest
from unittest import TestCase

from pig_latin import convert_to_pig_latin


class ConvertToPigLatingTestCase(unittest.TestCase):
    def test_word_that_starts_with_consonant(self):
        word = "rotten"
        converted_word = convert_to_pig_latin(word)
        self.assertEqual(converted_word, "ottenray")

    def test_word_that_starts_with_vowel(self):
        word = "eat"
        converted_word = convert_to_pig_latin(word)
        self.assertEqual(converted_word, "eatway")


if __name__ == "__main__":
    unittest.main()
