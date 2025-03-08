import unittest
from unittest.mock import Mock
from utilities.randomhelper import RandomHelper
from utilities.messagehelper import MessageHelper
from utilities.rsa import RSA

class TestRSA(unittest.TestCase):
    def setUp(self):
        self.random_handler = RandomHelper()
        self.message_handler = MessageHelper()
        self.rsa = RSA(self.random_handler)

    def test_rsa_works_in_a_random_scenario(self):
        message = "Test message for RSA algorithm."
        encoded_message = self.message_handler.string_to_int(message)
        keys = self.rsa.generate_keys()
        public_key = {"n": keys["n"], "exponent": keys["e"]}
        private_key = {"n": keys["n"], "exponent": keys["d"]}
        cipher = self.rsa.encrypt(encoded_message, public_key)
        back_to_encoded_message = self.rsa.decrypt(cipher, private_key)
        back_to_message = self.message_handler.int_to_string(back_to_encoded_message)
        self.assertEqual(message, back_to_message)

    def test_rsa_works_with_max_length_message(self):
        message = "." * 256
        encoded_message = self.message_handler.string_to_int(message)
        keys = self.rsa.generate_keys()
        public_key = {"n": keys["n"], "exponent": keys["e"]}
        private_key = {"n": keys["n"], "exponent": keys["d"]}
        cipher = self.rsa.encrypt(encoded_message, public_key)
        back_to_encoded_message = self.rsa.decrypt(cipher, private_key)
        back_to_message = self.message_handler.int_to_string(back_to_encoded_message)
        self.assertEqual(message, back_to_message)

    def test_rsa_unicodedecodeerror_with_too_long_message(self):
        message = "." * 257
        encoded_message = self.message_handler.string_to_int(message)
        keys = self.rsa.generate_keys()
        public_key = {"n": keys["n"], "exponent": keys["e"]}
        private_key = {"n": keys["n"], "exponent": keys["d"]}
        cipher = self.rsa.encrypt(encoded_message, public_key)
        back_to_encoded_message = self.rsa.decrypt(cipher, private_key)
        self.assertRaises(UnicodeDecodeError, self.message_handler.int_to_string, back_to_encoded_message)
