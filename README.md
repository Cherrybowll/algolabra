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
[6](https://github.com/Cherrybowll/algolabra/blob/main/documentation/weekreports/weekreport6.md)

## User instructions as of week 6

### Installation

This project requires Poetry and Python version ^3.10

1. Clone the repository to your device
2. Navigate to the repository root
3. Install dependencies with the command `poetry install`
4. (Optionally) activate the Poetry shell with the command `poetry start` (use `poetry exit` to exit when finished).
   - This step allows you to avoid typing `poetry run` before the commands in the manual.

### Manual

This takes precedence currently, ignore what the in-application UI says. Should be mostly the same, though.

- Start the program by running `invoke start`
- Once the program is running:
  - Generate a new key with the command `generate [key_name]`
  - Encrypt a message with the command `encrypt [key_name] [message]`
  - Decrypt a message with the command `decrypt [key_name] [message]`
  - Get help regarding a command with the command `help [command]`

**NB!** The encryption key is the public key, which is called "[key_name]_pub". The decryption key is the private key, which is simply called [key_name].
In its current state, the program is likely to crash with some poor inputs (like missing parameters).

Multiword messages must be encased in parentheses or only the symbols preceding the first whiteplace will be encrypted. Parentheses in the message can be escaped with backslash as per usual.
