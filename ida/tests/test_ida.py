import unittest
import ida

class TestIda(unittest.TestCase):

    def test_sum_all_even(self):
        test_in = [3, 7, 0, 3, 10, 4, 9, 12, 11, 13, 8]

        result = ida.sum_all_even(test_in)

        self.assertEqual(result, 34)

    def test_sum_all_even_2(self):
        test_in = [3, 7, 0, 3, 10, 4, 9, 12, 11, 13, 8, 5, 2]

        result = ida.sum_all_even(test_in)

        self.assertEqual(result, 36)

    def test_count_characters(self):

        test_senc = "Count the characters in this sentence"
        test_char = ['a', 'z', 's', 'r', 'n']

        result = ida.count_characters(test_senc, test_char)

        test_map = {'a': 2, 'z': 0, 's': 3, 'r': 2, 'n': 4}

        self.assertEqual(result, test_map)

    def test_count_characters_2(self):

        test_senc = "Traceback (most recent call last):"
        test_char = ['a', 'z', 's', 'r', 'n']

        result = ida.count_characters(test_senc, test_char)

        test_map = {'a': 4, 'z': 0, 's': 2, 'r': 2, 'n': 1}

        self.assertEqual(result, test_map)

    def test_reserve_sentence(self):

        test_senc = ["Count the characters in this sentence"]

        test_result = ["sentence this in characters the Count"]

        result = ida.reserve_sentence(test_senc)
        self.assertEqual(test_result, result)

    def test_difference_between_lists_1(self):

        list_1 = [ 2, 5, 8, 2, 1]
        list_2 = [ 2, 6, 9, 3, 4]

        test = [ 4, 11, 17, 5, 5]

        result = ida.list_difference(list_1, list_2)

        self.assertEqual(test, result)

    def test_reserve_order_diff(self):
        
        list_1 = [ 2, 5, 8, 2, 1]
        list_2 = [ 2, 6, 9, 3, 4]

        test = [ 3, 8, 17, 8, 4]

        result = ida.reserve_list_difference(list_1, list_2)

        self.assertEqual(test, result)
