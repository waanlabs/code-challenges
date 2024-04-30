"""
This module contains test case for Advent of Code (AoC) 2022 - Day 1.

Package: code_challenges
Subpackage: tests/y2k22/day_1
File: test_calorie_counter.py
Author: Waan <admin@waan.email>
Version: 1.0.0
Created: 01/12/2022
Modified: 12/04/2024 by admin@waan.email
"""

import unittest

from code_challenges.aoc.y2k22.day_1.count_calories_oop import CountCalories


class TestCountCaloriesOop(unittest.TestCase):
    """
    A test case for the CalorieCounter class.

    This test case contains multiple test methods to verify the functionality of the CalorieCounter
    class. It tests various methods and attributes of the CalorieCounter class, such as the puzzle
    file path getter and setter, the read_and_process method, the max_group_sum method, and the
    sum_of_largest_three method.

    max_group_sum: int
        The expected maximum sum of calorie groups.
    sum_of_largest_three: int
        The expected sum of the three largest calorie groups.
    file_path: str
        The file path of the puzzle input.

    Methods
    -------
    setUp():
        Set up the test environment before each test case.
    test_puzzle_file_path_getter():
        Test case to verify the getter method for the puzzle file path.
    test_puzzle_file_path_setter():
        Test case to verify the setter method for the puzzle file path.
    test_puzzle_file_path_setter_empty_string():
        Test case to verify that a ValueError is raised when an empty string is passed as the
        puzzle file path.
    test_puzzle_file_path_setter_invalid_string():
        Test case to verify the behavior of the puzzle_file_path setter when an invalid string is
        provided.
    test_read_and_process():
        Test case to verify the functionality of the read_and_process method.
    test_max_group_sum():
        Test case for the max_group_sum method of the CalorieCounter class.
    test_sum_of_largest_three():
        Test case to verify the correctness of the sum_of_largest_three method in the
        CalorieCounter class.
    """

    max_group_sum = 67633
    sum_of_largest_three = 199628
    file_path = "./code_challenges/aoc/y2k22/day_1/puzzle-input.txt"
    fake_file_path = "./code_challenges/aoc/y2k22/day_1/fake-input.txt"

    def setUp(self) -> None:
        """
        Set up the test environment before each test case.

        This method is called automatically before each test case is executed.
        It initializes the `calorie_counter` object, read and processe the data file.

        Returns:
            None
        """
        self.count_calories = CountCalories(self.file_path)

    def test_puzzle_file_path_getter(self) -> None:
        """
        Test case to verify the getter method for the puzzle file path.

        It sets the puzzle file path using the `puzzle_file_path` attribute of the
        `calorie_counter` object and then asserts that the getter method returns the same file path.

        Returns:
            None
        """
        self.assertEqual(self.count_calories.puzzle_file_path, self.file_path)

    def test_puzzle_file_path_setter(self) -> None:
        """
        Test case to verify the setter method for the puzzle file path.

        It sets the puzzle file path using the `puzzle_file_path` property of the `calorie_counter`
        object and asserts that the internal `_file_path` attribute is updated correctly.

        Returns:
            None
        """
        self.assertEqual(self.count_calories._file_path, self.file_path)

    def test_puzzle_file_path_setter_empty_string(self) -> None:
        """
        Test case to verify that a ValueError is raised when an empty string is passed as the
        puzzle file path.

        Returns:
            None
        """
        with self.assertRaises(ValueError):
            self.count_calories = CountCalories("")
            self.count_calories.read_calories()

    def test_puzzle_file_path_setter_invalid_type(self) -> None:
        """
        Test case to verify the behavior of the puzzle_file_path setter when an invalid string is
        provided.

        It should raise a TypeError when an invalid string is passed as the puzzle file
        path.

        Returns:
            None
        """
        with self.assertRaises(TypeError):
            self.count_calories = CountCalories(1234)
            self.count_calories.read_and_process()

    def test_puzzle_file_path_setter_fnf(self) -> None:
        """
        Test case to verify the behavior of the puzzle_file_path setter when the file does not
        exist.

        It should raise a FileNotFoundError when the file does not exist.

        Returns:
            None
        """
        with self.assertRaises(FileNotFoundError):
            self.count_calories = CountCalories("file_not_found.txt")
            self.count_calories.read_calories()

    def test_puzzle_file_path_deleter(self) -> None:
        """
        Test case to verify the behavior of the puzzle_file_path deleter.

        It asserts that the `_file_path` attribute is deleted after calling the deleter method.

        Returns:
            None
        """
        del self.count_calories.puzzle_file_path
        self.assertFalse(hasattr(self.count_calories, "_file_path"))

    def test_read_calories(self):
        calories_list = self.count_calories.read_calories()

        # Check that each item in the list is either an int or an empty string
        for item in calories_list:
            self.assertTrue(isinstance(item, int) or item == "")

        # Check that calories is a list
        self.assertIsInstance(calories_list, list)

    def test_read_calories_invalid_data(self) -> None:
        """
        Test case to verify the correctness of the read_calories method in the CalorieCounter class.

        It asserts that the returned calorie data is not None and has the correct length.

        Returns:
            None
        """
        with self.assertRaises(ValueError):
            self.count_calories = CountCalories(self.fake_file_path)
            self.count_calories.read_calories()

    def test_max_group_sum(self) -> None:
        """
        Test case for the max_group_sum method of the CalorieCounter class.

        It asserts that the result of the max_group_sum method is equal to the expected
        max_group_sum value.

        Returns:
            None
        """
        self.count_calories = CountCalories(self.file_path)
        calories_list = self.count_calories.read_calories()
        self.count_calories.process_calories(calories_list)
        self.assertEqual(self.count_calories.max_group_sum(), self.max_group_sum)

    def test_sum_of_largest_three(self) -> None:
        """
        Test case to verify the correctness of the sum_of_largest_three method in the
        CalorieCounter class.

        It asserts that the sum of the largest three elements returned by the method is equal to
        the expected sum.

        Returns:
            None
        """
        calories_list = self.count_calories.read_calories()
        self.count_calories.process_calories(calories_list)
        self.assertEqual(
            self.count_calories.sum_of_largest_three(), self.sum_of_largest_three
        )


if __name__ == "__main__":
    unittest.main()

"""
End of test_calorie_counter.py
"""
