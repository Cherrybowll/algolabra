import secrets
import random

def miller_rabin(n):
    """Function that performs the Miller-Rabin primality test for given integer n.

    Args:
        n (int): The integer the primality test is performed on. Should be odd.

    Returns:
        bool: Defines whether n is a probable prime.
    """

    if n < 4:

        if n == 2:
            return True
        
        if n == 3:
            return True
        
        if n < 2:
            return False

    if n % 2 == 0:
        return False

    # Factor (n - 1) to format 2^s*d, where
    # d is an odd positive integer and s is a positive integer.
    d = n - 1
    s = 0

    while d % 2 == 0:
        d = d // 2
        s += 1

    repeats = 40        # Higher value gives more accurate results
    cur_repeat = 1

    while cur_repeat <= repeats:

        # Random integer in range [2, n-2]
        a = secrets.randbelow(n - 1)
        if a < 2:
            continue

        cur_repeat += 1

        # x: congruence relation a^d == 1 (mod n)
        x = pow(a, d, n)
        y = 0

        for _ in range(s):

            # y: congruence relation a^((2^r)*d) == -1 (mod n)
            y = pow(x, 2, n)

            if y == 1 and x != 1 and x != n-1:
                return False
            x = y

        if y != 1:
            return False

    return True
