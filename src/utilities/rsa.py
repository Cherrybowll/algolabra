from .sieve_of_eratosthenes import sieve_of_eratosthenes
from .miller_rabin import miller_rabin
from .euclidean import euclidean

import secrets


class RSA:
    def __init__(self):
        pass

    def generate_keys(self):
        p, q = self._find_primes()
        n = p * q

    def encrypt(self):
        pass

    def decrypt(self):
        pass

    def _find_primes(self):
        small_primes = sieve_of_eratosthenes(5000)
        found_primes = []
        for _ in range(2):
            while True:
                testable_number = secrets.randbits(1024)
                not_a_prime = False

                for small_prime in small_primes:
                    if testable_number % small_prime == 0:
                        not_a_prime = True
                        break

                if not_a_prime:
                    continue

                if miller_rabin(testable_number):
                    found_primes.append(testable_number)
                    break

        return found_primes
