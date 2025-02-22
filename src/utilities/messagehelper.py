class MessageHelper:
    def string_to_int(self, input_string: str):
        return int.from_bytes(input_string.encode(), byteorder="little")

    def int_to_string(self, input_int: int):
        byte_length = (input_int.bit_length() + 7) // 8
        return input_int.to_bytes(byte_length, byteorder="little").decode()
