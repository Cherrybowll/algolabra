def sieve_of_eratosthenes(n):
    """Sieve of Eratosthenes -algorithm for generating a list of all prime numbers up to integer n.

    Args:
        n (int): Upper limit for the prime number value.

    Returns:
        list: A list of all prime numbers up to n.
    """

    marked = {}     # Dictionary for looking up integers that are determined non-prime.
    primes = []     # List of all found primes. Returned by the function.

    # Loop through all values from 2 to n.
    for i in range(2, n-1):
        if i in marked:
            continue

        primes.append(i)

        multiplier = 2
        marker = i * multiplier

        # Mark all multiples of i (smaller than n) since they can't be prime numbers.
        while marker <= n:
            marked[marker] = True
            multiplier += 1
            marker = i * multiplier

    return primes
