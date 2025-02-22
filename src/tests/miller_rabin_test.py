import unittest
from utilities.miller_rabin import miller_rabin

class TestMillerRabin(unittest.TestCase):
    def setUp(self):
        pass

    def test_miller_rabin_returns_false_for_even_numbers(self):
        self.assertEqual(miller_rabin(4), False)
        self.assertEqual(miller_rabin(2**1024), False)
        self.assertEqual(miller_rabin(6204642065390607545074574074276), False)

    def test_miller_rabin_returns_true_for_small_primes(self):
        self.assertEqual(miller_rabin(2), True)
        self.assertEqual(miller_rabin(3), True)
        self.assertEqual(miller_rabin(5), True)
        self.assertEqual(miller_rabin(5393), True)
        self.assertEqual(miller_rabin(7919), True)

    def test_miller_rabin_returns_true_for_large_primes(self):
        # Source: Wikipedia, Mersenne prime
        self.assertEqual(miller_rabin(2**1279-1), True)
        self.assertEqual(miller_rabin(2**2203-1), True)

    def test_miller_rabin_returns_false_for_one(self):
        self.assertEqual(miller_rabin(1), False)
    
    def test_miller_rabin_returns_false_for_zero(self):
        self.assertEqual(miller_rabin(0), False)

    def test_miller_rabin_returns_false_for_negatives(self):
        self.assertEqual(miller_rabin(-1), False)
        self.assertEqual(miller_rabin(-13), False)
        self.assertEqual(miller_rabin(-6), False)
