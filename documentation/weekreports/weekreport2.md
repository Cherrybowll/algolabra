# Week 2 report

## What I've done this week

- Implemented some of the algorithms that RSA uses:
  - Sieve of Eratosthenes, for calculating a bunch of small primes to optimize finding large primes
  - Miller-Rabin, for actually finding the large primes (or precisely, highly probable prime candidates)
  - Euclidean, for finding the greatest common divisor of two integers. Needed to calculate the Carmichael function of n (= pq, the primes)
- Setup the needed development dependencies to run unit tests and added some invoke tasks
- Made tests for the Euclidean algorithm
- Made a very early WIP version of the UI, currently quite dysfunctional

I also dedicated a decent amount of time to trying to understand the mathematical concepts behind the RSA algorithm. Pseudocode implementations for every part of the algorithm are readily available
on Wikipedia alone but it's boring and probably against the learning objectives of this course to just copy-paste the solutions without forming any understanding of the concepts.

## Project progress

The project progressed decently. I got many of the required 'sub-algorithms' of RSA working and started performing some unit testing too. I also envisioned the kind of text-interface I wish to use
and made a sort of MVP of it.

## What I learned

I learned a lot about the algorithms I implemented this week. Also researched interesting and associated properties of prime numbers and the modulo operation.

## Uncertainties and challenges

Nothing I currently need help with but I still lack in understanding some of the mathematical concepts. It's probably not required for the course but e.g. I'm trying to study the proof behind
recurrence of Carmichael totient function and why the composition property derives from it.

I also have to look into choosing the private key exponent e. Wikipedia says that 3 and preferably 65 537 work but at the moment I have no clue why.

## Plans for the next week

Continuing with key generation. So, more precisely, I'll be implementing the extended Euclidean algorithm after which I should have all the algorithms for key generation ready.
After that, I'll start looking into encryption and decryption, both of which appear far more trivial.

Also a lot of tests.

## Used hours

Around 13 hours I believe. Something between 10-15.
