def extended_euclidean(a : int, b: int):
    old_x, x = 1, 0
    old_y, y = 0, 1

    while b != 0:
        quotient = a // b
        a, b = b, a % b
        old_x, x = x, old_x - quotient * x
        old_y, y = y, old_y - quotient * x
    
    return {
        "gcd": abs(a),
        "coefficients": (abs(old_x), abs(old_y)),
        "quotients": (abs(y), abs(x))
    }
