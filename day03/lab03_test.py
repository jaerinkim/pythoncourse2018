import unittest
from lab03jaerin import *

class labTests(unittest.TestCase):
	## fill in a few tests for each
	## make sure to account for correct and incorrect input

    def test_shout(self):
        with self.assertRaises(TypeError): shout(2)
        self.assertEqual("CAPITAL LETTERS",shout("capital letters"))

    def test_reverse(self):
        with self.assertRaises(TypeError): reverse(2)
        self.assertEqual("reversed well",reverse("llew desrever"))


    def test_reversewords(self):
        with self.assertRaises(TypeError): reversewords(2)
        self.assertEqual("reversed words",reversewords("words reversed"))


    def test_reversewordletters(self):
        with self.assertRaises(TypeError): reversewordletters(2)
        self.assertEqual("confusing words",reversewordletters("gnisufnoc sdrow"))


    def test_piglatin(self):
        with self.assertRaises(TypeError): piglatin(2)
        self.assertEqual("igpay eaksspay",piglatin("pig speaks"))



if __name__ == '__main__':
  unittest.main()

