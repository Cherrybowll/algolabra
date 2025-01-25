def euclidean(a: int, b: int):
    """Implements the Euclidean algorithm, which returns the greatest
    common divisor of integers a and b.

    Args:
        a (int): Firt of the integers the GCD is calculated for.
        b (int): Second of the integers the GCD is calculated for.

    Returns:
        int: The greatest common divisor of integers a and b.
    """

    # Failsafes
    #if type(a) != int or type(b) != int:
        #raise TypeError("The given arguments must be positive integers")

    while b != 0:
        a, b = b, a % b

    return abs(a)

if __name__ == "__main__":
    print(euclidean(330, 631602))
