import unittest
from math_quiz import generate_random_integer, generate_random_choice, solve

class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_random_choice(self):
        choice = ['+', '-', '*']
        self.assertIn(generate_random_choice(),choice)

    def test_solve(self):
            test_cases =[
                (5, 2, '+', '5 + 2', 7),
                (5, 2, '-', '5 - 2', 3),
                (5, 5, '*', '5 * 5', 25),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                 self.assertTrue(expected_answer,solve(num1, num2, operator))

if __name__ == "__main__":
    unittest.main()
