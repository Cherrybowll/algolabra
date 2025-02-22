# Testing document

## Coverage report

Currently, the branch coverage is low-ish (68%), because integration testing is still missing (so in other words, `rsa.py` still requires testing). Miller-Rabin still needs some edge case testing for some known strong pseudoprimes.

![image](https://github.com/user-attachments/assets/e21319c9-548a-48e5-9e55-2c5220386b23)

## What is currently tested

This far all the auxiliary algorithms are tested. The tests are performed with the Python unittest library.
The tests use varying inputs, trying to account for edge cases and improper values.

For the extended Euclidean algorithm, it has been tested that parameters (0, 0) raise an ValueError
and that parameters (105, 2688) return the correct greatest common divisor (gcd) (21),
Bezout coefficients (-51, 2) and quotients by the gcd (5, 128).

Miller-Rabin is tested with integers of varying sizes, including small and large even and uneven composite numbers,
small and large prime numbers (including the actual use range of +1000 bit numbers) and negative numbers. Cases of strong pseudoprimes still require testing to guarantee full functionality.

## Running the tests

The tests can be run with command `poetry run invoke test`. The coverage report can be generated with the command
`poetry run invoke coverage-report`, which will also run the tests beforehand.
