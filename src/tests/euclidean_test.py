import unittest
from utilities.euclidean import euclidean

class TestEuclidean(unittest.TestCase):
    def setUp(self):
        pass

    def test_euclidean_works_1(self):
        a, b = 15, 75

        self.assertEqual(euclidean(a, b), 15)

    def test_euclidean_works_2(self):
        a, b = 537, 60426869469

        self.assertEqual(euclidean(a, b), 3)

    def test_euclidean_works_3(self):
        a, b = 505, 1

        self.assertEqual(euclidean(a, b), 1)

    def test_euclidean_works_big_primes(self):
        a = 31589724726762030927954968502003835603617239553751
        b = 79997781094623470974875659752950015720288694417393

        self.assertEqual(euclidean(a, b), 1)

    def test_euclidean_works_same_value(self):
        a, b = 123456, 123456

        self.assertEqual(euclidean(a, b), a)

    def test_euclidean_works_with_negatives(self):
        a, b = 56, -8

        self.assertEqual(euclidean(a, b), 8)

    def test_euclidean_fails_with_nonintegers(self):
        a, b = True, 5

        self.assertRaises(TypeError, euclidean, a, b)
