import secrets

class RandomHelper:
    def randbits_1024(self):
        return secrets.randbits(1022) + 2**1023 + 2**1022
