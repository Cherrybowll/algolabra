import unittest
from utilities.extended_euclidean import extended_euclidean


class TestExtendedEuclidean(unittest.TestCase):
    def setUp(self):
        pass

    def test_extended_euclidean_returns_correct_gcd(self):
        result = extended_euclidean(105, 2688)

        self.assertEqual(result["gcd"], 21)

    def test_extended_euclidean_returns_correct_coefficients(self):
        result = extended_euclidean(105, 2688)

        self.assertEqual(result["coefficients"], (-51, 2))

    def test_extended_euclidean_returns_correct_quotients(self):
        result = extended_euclidean(105, 2688)

        self.assertEqual(result["quotients"], (5, 128))

    def test_extended_euclidean_works_with_other_int_as_zero(self):
        result_zero_a = extended_euclidean(0, 10)
        result_zero_b = extended_euclidean(10, 0)

        self.assertEqual(result_zero_a["gcd"], 10)
        self.assertEqual(result_zero_a["coefficients"], (0, 1))
        self.assertEqual(result_zero_a["quotients"], (0, 1))

        self.assertEqual(result_zero_b["gcd"], 10)
        self.assertEqual(result_zero_b["coefficients"], (1, 0))
        self.assertEqual(result_zero_b["quotients"], (1, 0))

    def test_extended_euclidean_raises_value_error_with_both_zeros(self):
        self.assertRaises(ValueError, extended_euclidean, 0, 0)
