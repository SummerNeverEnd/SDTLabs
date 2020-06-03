import unittest
from all_here import *


class MyTestCase(unittest.TestCase):
    def test_input(self):
        some_text = Text()
        some_text.get_text_from_file()

        self.assertEqual(some_text.text, "Hi! I'm text analyzer and I'm going to work!\nBut I need your help, "
                                         "you just have to upgrade me!\nEOF")

    def test_func(self):
        some_text = Text()
        some_text.set_text_from_arg("a bb ccc")
        some_analyze = Analyzer(some_text)
        self.assertAlmostEqual(some_analyze.avg_word_length(), 2.0)

    def test_max(self):
        some_text = Text()
        some_text.set_text_from_arg("a bb ccc dd")
        some_analyze = Analyzer(some_text)
        self.assertAlmostEqual(some_analyze.max_len(), 3)

    def test_mode(self):
        some_text = Text()
        some_text.set_text_from_arg("a bb ccc dd")
        some_analyze = Analyzer(some_text)
        self.assertAlmostEqual(some_analyze.mode(), 2)


if __name__ == '__main__':
    unittest.main()


