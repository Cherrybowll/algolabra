# Specification document

Study program: Bachelor's programme in Computer Science (CS) / Tietojenkäsittelytieteen kandidaatti (TKT)

I will be implementing an RSA encrypter/decrypter with public/private key generation. Originally I wanted to make a Minesweeper solver but after hours of research I concluded that it might be too complex for my skill level.

The *core* of the project is to implement an encryption algorithm. Supporting algorithms will also be needed, more about them in the next chapter.

## Algorithms

The algorithms that will be implemented are

- **RSA** for key generation, encryption and decryption. This is sort of the 'main' algorithm for the project, the rest support the usage of RSA
- **Miller-Rabin** for finding large prime numbers for key generation
- **Sieve of Eratosthenes** for finding a set amount of smallest prime numbers to make usage of Miller-Rabin more efficient
- **Euclidean algorithm** for computing greatest common divisors
- **Extended euclidean algorithm** for computing the private key exponent (RSA)

Taken from the course topic page and [Wikipedia](https://en.wikipedia.org/wiki/RSA_(cryptosystem)).

## About languages

The project will be written entirely in Python.

Besides Python I _might_ be able to review projects written in Java.

The code and documentation will be written entirely in English (mostly for practice and concistency). I'm fluent in Finnish, so I can review projects in either language.

*I will present the finished work in Finnish in the demo session*.

## Inputs and outputs

The finished product should

- Generated and provide to the user a public and private RSA key when asked
- Given a message and a key, encrypt the user's message
- Given an encrypted message and a key, decrypt the message

## Time complexity

From what I've understood, the most significant factor in time complexity is finding potential large primes with Miller-Rabin algorithm, which has the time complexity of O(k * n^3) 
(according to [Wikipedia](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Complexity)).
