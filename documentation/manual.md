# User instructions

## Installation

This project requires Poetry and Python version ^3.10

1. Clone the repository to your device
2. Navigate to the repository root
3. Install dependencies with the command `poetry install`
4. (Optionally) activate the Poetry shell with the command `poetry start` (use `poetry exit` to exit when finished).
   - This step allows you to avoid typing `poetry run` before the commands in the manual.

## Manual

The user interface is quite clear and has a help command but here are all the commands regardless:

- Start the program by running `invoke start`
- Once the program is running:
  - Generate a new key with the command `generate [key_name]`
  - Encrypt a message with the command `encrypt [key_name] [message]`
  - Decrypt a message with the command `decrypt [key_name] [cipher]`
  - Get help regarding a command with the command `help [command]`

**NB!** The encryption key is the public key, which is called "[key_name]_pub". The decryption key is the private key, which is simply called [key_name].
The keys can also be used the other way around for message signing.

Multiword messages **MUST** be encased in parentheses or only the symbols preceding the first whitespace will be encrypted. Parentheses in the message can be escaped with backslash as per usual.
