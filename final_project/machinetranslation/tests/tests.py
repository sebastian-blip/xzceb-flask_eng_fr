import unittest
from translator import englishToFrench, frenchToEnglish


class TestTranslate(unittest.TestCase):
    def test_english_frech(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertNotEqual(englishToFrench('Hello'), 'Hello')

    def test_frech_english(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertNotEqual(frenchToEnglish('Bonjour'), 'Bonjour')

if __name__ == '__main__':
    unittest.main()
