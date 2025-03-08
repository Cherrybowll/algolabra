# Implementation document

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
- `MessageHelper`, which provides encoding and decoding of strings to integers using utf-8
- `RandomHelper`, which provides generating of random 1024 bit integers with the first to bits being 1, guaranteeing 2048 bit products

## References

- https://en.wikipedia.org/wiki/RSA_(cryptosystem)
- https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
- https://en.wikipedia.org/wiki/Euclidean_algorithm
- https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
- https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
- https://en.wikipedia.org/wiki/Mersenne_prime
- Various StackOverflow answers for tips and tricks
- [ozkanali357's](https://github.com/ozkanali357/AILabsProject) project on the same course, which I peer reviewed,
  for showing me a slightly faster and smarter way to calculate byte length from bit length without `math` dependency
