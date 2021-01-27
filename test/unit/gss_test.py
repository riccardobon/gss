""" Unit tests for gss_module"""
import unittest
from gss_module.gss import GoldenSectionSearch


class GoldenSectionSearchTestCase(unittest.TestCase):
    """ Tests for GoldenSectionSearch"""

    def setUp(self) -> None:
        """Initialize test class"""
        self.gss = GoldenSectionSearch()

    def test_none_on_empy_list(self) -> None:
        """Test for returning None if list is empty"""
        self.assertIsNone(self.gss.run([]))

    def test_none_on_one_element_list(self) -> None:
        """Test for returning None if list has just one element"""
        self.assertIsNone(self.gss.run([123.3]))

    def test_none_on_two_elements_list(self) -> None:
        """Test for returning None if list has just two elements"""
        self.assertIsNone(self.gss.run([123.3, 456.6]))

    def test_not_none_on_three_elements_list(self) -> None:
        """Test for not returning None if list has three elements"""
        self.assertIsNotNone(self.gss.run([123.3, 456.6, 789.9]))

    def test_minimum_on_positive_ints(self) -> None:
        """Test for minimum on positive integers"""
        self.assertEqual(self.gss.run([78, 23, 22, 21, 10, 4, 0, 1, 3, 11, 12,
                                       145]), 0)
        self.assertEqual(self.gss.run([787, 786, 4, 2, 1, 3, 11, 12, 13],
                                      True), 1)

    def test_maximum_on_positive_ints(self) -> None:
        """Test for maximum on positive integers"""
        self.assertEqual(self.gss.run([3, 23, 122, 2100, 2101, 2099, 150,
                                      11, 14, 0], False), 2101)

    def test_minimum_on_negative_ints(self) -> None:
        """Test for minimum on negative integers"""
        self.assertEqual(self.gss.run([-1, -2, -3, -10, -9, -3, -1]), -10)
        self.assertEqual(self.gss.run([-1, -2, -3, -10, -123, -122, -9, -3,
                                      -1], True), -123)

    def test_maxmum_on_negative_ints(self) -> None:
        """Test for maximum on negative integers"""
        self.assertEqual(self.gss.run([-44, -43, -22, -21, -11, -10, -11, -12,
                                      -100], False), -10)

    def test_minimum_on_ints(self) -> None:
        """Test for minimum on integers"""
        self.assertEqual(self.gss.run([30, 1, 0, -1, -2, -3, -10, -9, -3, -1,
                                      1, 1000]), -10)
        self.assertEqual(self.gss.run([30, 1, 0, -1, -10, -900, -3, -1, 1,
                                      20], True), -900)

    def test_maximum_on_ints(self) -> None:
        """Test for maximum on integers"""
        self.assertEqual(self.gss.run([-30, -1, 0, 1, 10, 900, -3, -1000,
                                      -20000], False), 900)

    def test_minimum_on_floats(self) -> None:
        """Test for minimum on floats"""
        self.assertEqual(self.gss.run([12.3, 12.2, 12.19999, 3, 2.9999, 3.0,
                                      3.1, 3.2, 3.3, 3.4, 5, 66, 777, 888]),
                         2.9999)
        self.assertEqual(self.gss.run([12.3, 12.2, 12.19999, 3, 2.9999, -3.0,
                                      -2.99999, 0, 2.2, 2.3, 3.4, 5], True),
                         -3.0)

    def test_maximum_on_floats(self) -> None:
        """Test for maximum on floats"""
        self.assertEqual(self.gss.run([-12.3, -2.2, 0, 0.00001, 0, -0.00001,
                                      -0.00002, -0.00003, -0.00004], False),
                         0.00001)

    def test_minimum_on_chars(self) -> None:
        """Test for minimum on chars"""
        self.assertEqual(self.gss.run(['h', 'f', 'e', 'c', 'b', 'i', 'j', 'k',
                                      'v', 'w', 'z']), 'b')
        self.assertEqual(self.gss.run(['h', 'f', 'e', 'c', 'b', 'a', 'b', 'c',
                                      'd', 'j', 'z'], True), 'a')

    def test_maximum_on_chars(self) -> None:
        """Test for maximum on chars"""
        self.assertEqual(self.gss.run(['a', 'b', 'c', 'd', 'e', 'f', 't', 'r',
                                      'g', 'd', 'b'], False), 't')

    def test_minimum_on_strings(self) -> None:
        """Test for minimum on strings"""
        self.assertEqual(self.gss.run(['strawberry', 'kiwi', 'cherry',
                                      'blueberry', 'banana', 'apple',
                         'avocado', 'mango', 'orange', 'pear']), 'apple')
        self.assertEqual(self.gss.run(['sweden', 'spain', 'france', 'canada',
                                      'china', 'finland', 'japan',
                         'new zealand'], True), 'canada')

    def test_maximum_on_strings(self) -> None:
        """Test for maximum on strings"""
        self.assertEqual(self.gss.run(['black', 'blue', 'cyan', 'magenta',
                                      'red', 'yellow', 'pink', 'green',
                         'brown'], False), 'yellow')


if __name__ == '__main__':
    unittest.main()
