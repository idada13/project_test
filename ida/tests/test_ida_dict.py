import unittest
import ida

class TestIda(unittest.TestCase):
    

    def test_1(self):
        input_value = {
            "AAA": "Test1",
            "AAB": "test_A",
            "ABA": "test_B",
            "ABB": "test_R",
            "BAA": "Test2",
            "BAB": "TEST_z",
            "BBA": "TEST56"
        }
        
        result = ["AAA", "BAA", "BBA"]

        self.assertEqual(ida.extract_keys_with_numbers(input_value), result)



    def test_1(self):
        input_value_1 = {
            "AAA": "Test1",
            "AAB": "test_A",
            "ABA": "test_B",
        }

        input_value_2 = {
            "ABB": "test_R",
            "BAA": "Test2",
            "BAB": "TEST_z",
            "BBA": "TEST56"
        }

        input_value_3 = {
            "ABC": "test_R",
            "BAC": "Test2",
            "BAB": "TEST_zkj",
            "BBS": "TEST56"
        }

        input_value_4 = {
            "ABC": "test_R",
            "AAB": "Test2",
            "BAZ": "TEST_z",
            "BBA": "TEST56_a"
       }

        value_in = [ input_value_1, input_value_2, input_value_3, input_value_4]

        
        result = {
            "AAA": "Test1",
            "AAB": "conflict",
            "ABA": "test_B",
            "ABB": "test_R",
            "BAA": "Test2",
            "BAB": "conflict",
            "BBA": "Conflict",
            "ABC": "test_R",
            "BAC": "Test2",
            "BBS": "TEST56",
            "BAZ": "TEST_z"
        }

        self.assertEqual(ida.merge_dicts(value_in), result)
