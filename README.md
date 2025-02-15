# RSA encrypter/decrypter

For the course *Algoritmit ja tekoäly* (HY)

## Documentation

- [Specification document](https://github.com/Cherrybowll/algolabra/blob/main/documentation/specification.md)
- [Testing document](https://github.com/Cherrybowll/algolabra/blob/main/documentation/tests.md)
- [Implementation document](https://github.com/Cherrybowll/algolabra/blob/main/documentation/implementation.md)
- [Week reports](https://github.com/Cherrybowll/algolabra/tree/main/documentation/weekreports),
[1](https://github.com/Cherrybowll/algolabra/blob/main/documentation/weekreports/weekreport1.md)
[2](https://github.com/Cherrybowll/algolabra/blob/main/documentation/weekreports/weekreport2.md)
[3](https://github.com/Cherrybowll/algolabra/blob/main/documentation/weekreports/weekreport3.md)
[4](https://github.com/Cherrybowll/algolabra/blob/main/documentation/weekreports/weekreport4.md)
[5](https://github.com/Cherrybowll/algolabra/blob/main/documentation/weekreports/weekreport5.md)

## User instructions as of week 4

### Installation

This project requires Poetry and Python version ^3.10

1. Clone the repository to your device
2. Navigate to the repository root
3. Install dependencies with the command `poetry install`
4. (Optionally) activate the Poetry shell with the command `poetry start` (use `poetry exit` to exit when finished).
   - This step allows you to avoid typing `poetry run` before the commands in the manual.

### Manual

This takes precedence currently, ignore what the in-application UI says.

- Start the program by running `invoke start`
- Once the program is running:
  - Generate a new key with the command `generate [key_name]`
  - Encrypt a message with the command `encrypt [message] [key_name]`
  - Decrypt a message with the command `decrypt [message] [key_name]`

**NB!** The encryption key is the public key, which is called "[key_name]_pub". The decryption key is the private key, which is simply called [key_name]. Attempting to decrypt with the public key should guaranteedly crash the program as of now.
Many other things also probably crash the program as of now.

Also note that the messages are INTEGERS. Non-numeral inputs crash the program. Lots of things crash the program.
