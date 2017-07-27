def remove_duplicates(word):
	word_list = list(word)
	new_list= []
	for item in word_list:
		test = True
		for item2 in new_list:
			if item is item2:
				test = False
				break

		if test == True:
			new_list.append(item)
	output = ""
	for item in new_list:
		output = output+str(item)
	
	tuple = ((''.join(sorted(output))), (len(word_list)- len(new_list)))
	
	return tuple


import unittest
class Test(unittest.TestCase):
    def test_output_is_correct(self):
        result1 = remove_duplicates('aaabbbac')
        result2 = remove_duplicates('a')
        result3 = remove_duplicates('thelexash')

        self.assertIsInstance(result1, tuple, msg='Incorrect output type')
        self.assertEqual(result1, ('abc', 5), msg='Incorrect output')

        self.assertIsInstance(result2, tuple, msg='Incorrect output type')
        self.assertEqual(result2, ('a', 0), msg='Incorrect output')

        self.assertIsInstance(result3, tuple, msg='Incorrect output type')
        self.assertEqual(result3, ('aehlstx', 2), msg='Incorrect output')

    def test_output_is_correct_hidden(self):
        result1 = remove_duplicates('thisisateststring')
        result2 = remove_duplicates('letsseehowthisgoes')
        result3 = remove_duplicates('hiddenhiddenhiddenhaha')

        self.assertIsInstance(result1, tuple, msg='Incorrect output type')
        self.assertEqual(result1, ('aeghinrst', 8), msg='Incorrect output')

        self.assertIsInstance(result2, tuple, msg='Incorrect output type')
        self.assertEqual(result2, ('eghilostw', 9), msg='Incorrect output')

        self.assertIsInstance(result3, tuple, msg='Incorrect output type')
        self.assertEqual(result3, ('adehin', 16), msg='Incorrect output')

unittest.main()