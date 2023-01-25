import unittest
freom translator import english_to_french, french_to_english 

class TestE2F(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('Hello'), 'Bonjour')


class TestF2E(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()
