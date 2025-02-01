# Testing document

## Coverage report

Currently, the branch coverage is quite low (29%), since Miller-Rabin still needs planning for the tests and `rsa.py`
will only be tested once all the underlying algorithms are completely ready (since it will kind of integration testing).

![image](https://github.com/user-attachments/assets/e21319c9-548a-48e5-9e55-2c5220386b23)

## What is currently tested

This far all the auxiliary algorithms besides Miller-Rabin are tested. The tests are performed with the Python unittest library.
The tests use varying inputs, trying to account for edge cases and improper values.

For the extended Euclidean algorithm, it has been tested that parameters (0, 0) raise an ValueError and that parameters (105, 2688)
return the correct greatest common divisor (gcd) (21), Bezout coefficients (-51, 2) and quotients by the gcd (5, 128).

## Running the tests

The tests can be run with command `poetry run invoke test`. The coverage report can be generated with the command
`poetry run invoke coverage-report`, which will also run the tests beforehand.
