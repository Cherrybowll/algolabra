def extended_euclidean(a: int, b: int):
    """Implements the extended Euclidean algorithm for calculating the greatest common divisor between two integers a and b. Additionally calculates the Bezout coefficients and quotients of a and by by the gcd.

    Args:
        a (int): One of the integers to calculate gcd for
        b (int): One of the integers to calculate gcd for

    Raises:
        ValueError: Both integers passed as parameters are zero.

    Returns:
        dict: gcd stores the greatest common divisor, coefficients stores the Bezout coefficients and quotients stores the coefficients of a and b by their greatest common divisor.
    """

    # Failsafe for the edge case gcd(0, 0), which isn't properly defined
    if a == 0 and b == 0:
        raise ValueError(
            "Greatest common divisor is not defined for two zeros.")

    old_x, x = 1, 0
    old_y, y = 0, 1

    while b != 0:
        quotient = a // b
        a, b = b, a % b
        old_x, x = x, old_x - quotient * x
        old_y, y = y, old_y - quotient * y

    return {
        "gcd": abs(a),
        "coefficients": (old_x, old_y),
        "quotients": (abs(y), abs(x))
    }
