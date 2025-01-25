def euclidean(a: int, b: int):
    """Implements the Euclidean algorithm, which returns the greatest
    common divisor of integers a and b.

    Args:
        a (int): Firt of the integers the GCD is calculated for.
        b (int): Second of the ntegers the GCD is calculated for.

    Returns:
        int: The greatest common divisor of integers a and b.
    """

    # Failsafes
    if type(a) != int or type(b) != int:
        raise TypeError("The given arguments must be positive integers")

    if a < 1 or b < 1:
        raise ValueError("The given arguments must be positive integers")

    while a != b:
        if a > b:
            a -= b
        else:
            b -= a

    return a
