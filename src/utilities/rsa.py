from .sieve_of_eratosthenes import sieve_of_eratosthenes
from .miller_rabin import miller_rabin
from .euclidean import euclidean

import secrets


class RSA:
    def __init__(self):
        self.e = 65537

    def generate_keys(self):
        p, q = self._find_primes()
        n = p * q
        n_totient = abs((p-1)*(q-1))/euclidean(p-1, q-1)

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
                    print(testable_number.bit_length())
                    break

        return found_primes

    def _check_suitable_totient(self, totient: int, e: int):
        return euclidean(totient, e) == 1

    def _check_primes_sufficient_distance(self, p: int, q: int):
        # In here as a placeholder
        # Still contemplating whether checking the prime value difference is meaningful
        # The possibility of the primes being too close to one another is
        # sort of negligible.
        pass


if __name__ == "__main__":
    my_rsa = RSA(65537)
    my_primes = my_rsa._find_primes()
    for prime in my_primes:
        print(prime.bit_length())
    print("n:", (my_primes[0]*my_primes[1]).bit_length())
