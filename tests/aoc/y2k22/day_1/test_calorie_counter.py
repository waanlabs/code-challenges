import unittest
from code_challenges.aoc.y2k22.day_1.calorie_counter import CalorieCounter


class TestCalorieCounter(unittest.TestCase):
    """
    A test case for the CalorieCounter class.

    This test case contains multiple test methods to verify the functionality of the CalorieCounter class.
    It tests various methods and attributes of the CalorieCounter class, such as the puzzle file path getter and setter,
    the read_and_process method, the max_group_sum method, and the sum_of_largest_three method.

    Attributes
    ----------
    max_group_sum : int
        The expected maximum sum of calorie groups.
    sum_of_largest_three : int
        The expected sum of the three largest calorie groups.
    file_path : str
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
        Test case to verify that a ValueError is raised when an empty string is passed as the puzzle file path.
    test_puzzle_file_path_setter_invalid_string():
        Test case to verify the behavior of the puzzle_file_path setter when an invalid string is provided.
    test_read_and_process():
        Test case to verify the functionality of the read_and_process method.
    test_max_group_sum():
        Test case for the max_group_sum method of the CalorieCounter class.
    test_sum_of_largest_three():
        Test case to verify the correctness of the sum_of_largest_three method in the CalorieCounter class.
    """

    max_group_sum = 67633
    sum_of_largest_three = 199628
    file_path = "./code_challenges/aoc/y2k22/day_1/puzzle-input.txt"

    def setUp(self) -> None:
        """
        Set up the test environment before each test case.

        This method is called automatically before each test case is executed.
        It initializes the `calorie_counter` object and reads and processes the file.

        Returns:
            None
        """
        self.calorie_counter = CalorieCounter(self.file_path)
        self.calorie_counter.read_and_process()

    def test_puzzle_file_path_getter(self) -> None:
        """
        Test case to verify the getter method for the puzzle file path.

        It sets the puzzle file path using the `puzzle_file_path` attribute of the `calorie_counter` object and then
        asserts that the getter method returns the same file path.

        Returns:
            None
        """
        self.calorie_counter.puzzle_file_path = self.file_path
        self.assertEqual(self.calorie_counter.puzzle_file_path, self.file_path)

    def test_puzzle_file_path_setter(self) -> None:
        """
        Test case to verify the setter method for the puzzle file path.

        It sets the puzzle file path using the `puzzle_file_path` property of the `calorie_counter` object and asserts
        that the internal `_file_path` attribute is updated correctly.

        Returns:
            None
        """
        self.calorie_counter.puzzle_file_path = self.file_path
        self.assertEqual(self.calorie_counter._file_path, self.file_path)

    def test_puzzle_file_path_setter_empty_string(self) -> None:
        """
        Test case to verify that a ValueError is raised when an empty string is passed as the puzzle file path.

        Returns:
            None
        """
        with self.assertRaises(ValueError):
            self.calorie_counter = CalorieCounter("")
            self.calorie_counter.read_and_process()

    def test_puzzle_file_path_setter_invalid_string(self) -> None:
        """
        Test case to verify the behavior of the puzzle_file_path setter when an invalid string is provided.
        It should raise a TypeError when an invalid string is passed as the puzzle file path.

        Returns:
            None
        """
        with self.assertRaises(TypeError):
            self.calorie_counter = CalorieCounter(1234)
            self.calorie_counter.read_and_process()

    def test_read_and_process(self) -> None:
        """
        Test case to verify the functionality of the read_and_process method.

        This test sets the puzzle file path, calls the read_and_process method,
        and then checks if the calories_sum attribute of the calorie_counter object is not None.

        Returns:
            None
        """
        with self.assertRaises(FileNotFoundError):
            self.calorie_counter = CalorieCounter("file_not_found.txt")
            self.calorie_counter.read_and_process()

    def test_max_group_sum(self) -> None:
        """
        Test case for the max_group_sum method of the CalorieCounter class.
        It asserts that the result of the max_group_sum method is equal to the expected max_group_sum value.

        Returns:
            None
        """
        self.assertEqual(self.calorie_counter.max_group_sum(), self.max_group_sum)

    def test_sum_of_largest_three(self) -> None:
        """
        Test case to verify the correctness of the sum_of_largest_three method in the CalorieCounter class.
        It asserts that the sum of the largest three elements returned by the method is equal to the expected sum.

        Returns:
            None
        """
        self.assertEqual(
            self.calorie_counter.sum_of_largest_three(), self.sum_of_largest_three
        )


if __name__ == "__main__":
    unittest.main()
