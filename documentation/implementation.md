# Implementation document

This is very much a work in progress and parts are purposely left out, since I fear the contents might go through some quite major changes.

## Structure

The program is currently structured as follows (not counting `index.py`, which only creates an instance of the UI and RSA tools):
- Utilities (directory which holds the algorithms)
  - `RSA` is the main application logic, which handles key generation and message encryption/decryption
  - Subalgorithms, that `RSA` calls to fulfill its purpose
    - `sieve_of_eratosthenes`
    - `euclidean`
    - `extended_euclidean`
    - `miller_rabin`
- `UI`, which manages I/O between the user and the algorithm. Also a bit oddly handles writing/reading files
- `FileHelper`, which provides the functionalities for reading/writing files to the UI

## References

- https://en.wikipedia.org/wiki/RSA_(cryptosystem)
- https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
- https://en.wikipedia.org/wiki/Euclidean_algorithm
- https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
- https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
