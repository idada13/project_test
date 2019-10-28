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
        
        result = [("AAA", "Test1"),
            ("AAB", "test_A"),
            ("ABA", "test_B"),
            ("ABB", "test_R"),
            ("BAA", "Test2"),
            ("BAB", "TEST_z"),
            ("BBA", "TEST56")]

        self.assertEqual(ida.turn_dict_to_list(input_value), result)

    def test_2(self):
        result = {
            "AAA": "Test1",
            "AAB": "test_A",
            "ABA": "test_B",
            "ABB": "test_R",
            "BAA": "Test2",
            "BAB": "TEST_z",
            "BBA": "TEST56"
        }
        
        input_value = [("AAA", "Test1"),
            ("AAB", "test_A"),
            ("ABA", "test_B"),
            ("ABB", "test_R"),
            ("BAA", "Test2"),
            ("BAB", "TEST_z"),
            ("BBA", "TEST56")]

        self.assertEqual(ida.turn_list_into_dict(input_value), result)

    def test_3(self):
        input_1 = {
            "AAA": "Test1",
            "AAB": "test_A",
            "ABA": "test_B",
            "ABB": "test_R",
            "BAA": "Test2",
            "BAB": "TEST_z",
            "BBA": "TEST56"
        }
        
        input_2 = {
            "CCC": "Zandom",
            "CCA": "Random",
            "CAC": "Fandom",
            "CAA": "test_R",
            "AAA": "Kandom",
            "CCB": "TEST_z",
            "CBC": "TEST56"
        }
        
        input_3 = {
            "ZZZ": "uZandom",
            "ZZA": "uRandom",
            "ZZB": "Fandom",
            "ZZC": "utest_R",
            "ZZD": "Kandom",
            "ZZE": "TEST_z",
            "23S": "uTEST56"
        }

        input_value = [input_1, input_2, input_3]

        result = {
                "test_R": ["ABB", "CCA"],
                "TEST_Z": ["BAB", "CCB", "ZZE"],
                "TEST56": ["BBA", "CBC"],
                "Fandom": ["CAC", "ZZB"],
                "Kandom": ["AAA", "ZZD"]

                }
 
        self.assertEqual(ida.return_dict_with_matching_values(input_value), result)


