import camelCase
from unittest import TestCase

class TestCamelCase(TestCase):

    def test_camelcase_sentence(self):

        input_and_expected_outputs = {
        '':'',
        'helLo WoRld':'helloWorld',
        'HellO WorlD':'helloWorld',
        'hello world':'helloWorld',
        'heLLo wORLD':'helloWorld',
        'かまは らがわし にくすむ ゆへめ':'かまはらがわしにくすむゆへめ',
        '♥☻ is a heart and a smiley face':'♥☻IsAHeartAndASmileyFace',
        }

        for input_val in input_and_expected_outputs.keys():
            self.assertEqual(input_and_expected_outputs[input_val], camelCase.modify_sentence(input_val))

if __name__ == '__main__':
    import unittest
    unittest.main()
