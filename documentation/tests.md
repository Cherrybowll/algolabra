# Testing document

## Coverage report

The branch coverage is 96% as can be seen from the image below.

![image](https://github.com/user-attachments/assets/8eecec01-c3ed-4567-b72f-a5904b459514)

## What is tested

All the auxiliary algorithms are unit tested. The tests are performed with the Python unittest library.
The tests use varying inputs, trying to account for edge cases and improper values.

For the extended Euclidean algorithm, it has been tested that parameters (0, 0) raise an ValueError
and that parameters (105, 2688) return the correct greatest common divisor (gcd) (21),
Bezout coefficients (-51, 2) and quotients by the gcd (5, 128).

Miller-Rabin is tested with integers of varying sizes, including small and large even and uneven composite numbers,
small and large prime numbers (including the actual use range of +1000 bit numbers) and negative numbers.

End-to-end testing is done through the `rsa.py` file and additionally with `messagehelper.py` for translating between strings and their integer representations.

## Running the tests

The tests can be run with command `poetry run invoke test`. The coverage report can be generated with the command
`poetry run invoke coverage-report`, which will also run the tests beforehand.
