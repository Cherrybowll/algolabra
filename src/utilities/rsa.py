from .sieve_of_eratosthenes import sieve_of_eratosthenes
from .miller_rabin import miller_rabin
from .euclidean import euclidean
from .extended_euclidean import extended_euclidean

import secrets


class RSA:
    """Class that implements the RSA algorithm, including key generation, encryption and decryption.
    """

    def __init__(self):
        pass

    def generate_keys(self):
        """Generates a public-private RSA key.

        Returns:
            dict: Parts of the key with product of primes as 'n',
            public exponent as 'e' and private exponent as 'd'.
        """

        p, q = self._find_primes()
        n = p * q
        n_totient = abs((p-1)*(q-1)) // euclidean(p-1, q-1)

        # Public exponent
        e = 65537

        #Private exponent
        d = extended_euclidean(e, n_totient)["coefficients"][0]

        return {"n": n, "e": e, "d": d}

    def encrypt(self, message, key):
        """Encrypts/signs a message with the selected key.

        Args:
            message (int): Integer representation of the message to be encrypted.
            key (dict): Dictionary with keys 'n' and 'exponent'.

        Returns:
            int: The encrypted/signed message.
        """

        return pow(message, key["exponent"], key["n"])

    def decrypt(self, cipher, key):
        """Decrypts a message with the selected key.

        Args:
            cipher (int): The integer cipher of the original message.
            key (dict): Dictionary with keys 'n' and 'exponent'.

        Returns:
            int: The decrypted message.
        """

        return pow(cipher, key["exponent"], key["n"])

    def _find_primes(self):
        """Private method for finding large prime numbers for key generation.

        Returns:
            tuple: A tuple with two large prime numbers.
        """

        small_primes = sieve_of_eratosthenes(5000)
        found_primes = []

        for _ in range(2):
            while True:

                # Guarantees that the prime is exactly 1024 bits long and
                # that n will be exactly 2048 bits long
                testable_number = secrets.randbits(1022) + 2**1023 + 2**1022

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

    def _check_suitable_totient(self, totient: int, e: int):
        """Private method for checking that the totient of n is coprime with the public exponent e.

        Args:
            totient (int): Totient of n, the product of the large primes used for key generation.
            e (int): The public exponent of the key.

        Returns:
            bool: Whether the check passes.
        """

        return euclidean(totient, e) == 1

    def _check_primes_sufficient_distance(self, p: int, q: int):
        # In here as a placeholder
        # Still contemplating whether checking the prime value difference is meaningful
        # The possibility of the primes being too close to one another is
        # sort of negligible.
        pass


if __name__ == "__main__":
    my_rsa = RSA()
    my_primes = my_rsa._find_primes()
    for prime in my_primes:
        print(prime.bit_length())
    print("n:", (my_primes[0]*my_primes[1]).bit_length())
