import unittest
from utilities.sieve_of_eratosthenes import sieve_of_eratosthenes

class TestSieveOfEratosthenes(unittest.TestCase):
    def setUp(self):
        pass

    def test_sieve_of_eratosthenes_works_with_limit_ten(self):
        primes = sieve_of_eratosthenes(10)

        self.assertEqual(primes, [2, 3, 5, 7])

    def test_sieve_of_eratosthenes_works_with_limit_one(self):
        primes = sieve_of_eratosthenes(1)

        self.assertEqual(primes, [])

    def test_sieve_of_eratosthenes_returns_empty_list_for_negative_limit(self):
        primes = sieve_of_eratosthenes(-100)

        self.assertEqual(primes, [])

    def test_sieve_of_eratosthenes_finds_five_600_smallest_primes(self):
        # 600th prime starting from 2 is 4409, 601st is 4421
        primes = sieve_of_eratosthenes(4420)

        self.assertEqual(len(primes), 600)
        self.assertEqual(primes[-1], 4409)

    def test_sieve_of_eratosthenes_works_with_a_largish_value(self):
        # Testing for the biggest known Fermat prime (65537) + 1
        primes = sieve_of_eratosthenes(65538)

        self.assertEqual(primes[-1], 65537)
