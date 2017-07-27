def longest(sentence):
	words = sentence.split()
	lengths = []
	for word in words:
		lengths.append(len(word))

	maximum = max(lengths)
	for word in words:
		if len(word) == maximum:
			return word
			break

import unittest;

class Test(unittest.TestCase):
     def test_longest_word(self):
            sentence = "This is Andela"
            self.assertEqual('Andela', longest(sentence))

     def test_one_word(self):
            sentence = "This"
            self.assertEqual("This", longest(sentence))

unittest.main()