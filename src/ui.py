import shlex

class UI:
    def __init__(self, rsa_handler, file_handler, message_handler):
        self._rsa = rsa_handler
        self._files = file_handler
        self._messages = message_handler

    def start(self):
        while True:
            print("RSA tool running, enter command:\n\n"
                  f"{'generate':15}{'[name]':15}\n"
                  f"{'encrypt':15}{'[key]':15}{'[message]':15}\n"
                  f"{'decrypt':15}{'[key]':15}{'[cipher]':15}\n"
                  f"{'help':15}{'[command]':15}\n"
                  "exit")
            user_input = self._parse_command(input("> "))

            #Failsafe if user enters nothing or only whitespaces
            if len(user_input) == 0:
                continue

            command, params = user_input[0], user_input[1:]

            match command:
                case "generate":
                    self._generate(params)
                case "encrypt":
                    self._encrypt(params)
                case "decrypt":
                    self._decrypt(params)
                case "help":
                    self._help(params)
                case "exit":
                    print("Exiting...")
                    break
                case _:
                    self._pretty_output(f"Command {command} is not recognized.\n")

    def _generate(self, params):
        if len(params) == 0:
            pass

        key_name = params[0]

        self._files.check_key_exist(key_name)
        key_parts = self._rsa.generate_keys()
        public_key = (key_parts["n"], key_parts["e"])
        private_key = (key_parts["n"], key_parts["d"])
        self._files.create_key(key_name, private_key, True)
        self._files.create_key(key_name + "_pub", public_key, True)
        output = f"Public-private key pair {key_name} and {key_name}_pub were generated in data directory.\n"
        self._pretty_output(output)

    def _encrypt(self, params):
        try:
            if len(params) == 0:
                pass

            key_name, message = params[0], params[1]

            if not self._files.check_key_exist(key_name):
                pass

            messageint = self._messages.string_to_int(message)

            key_parts = self._files.get_key(key_name)
            key = {"n": key_parts[0], "exponent": key_parts[1]}
            cipher = self._rsa.encrypt(messageint, key)
            self._pretty_output(f"{cipher}\n")
        except:
            self._pretty_output("Encryption unsuccesful\n")

    def _decrypt(self, params):
        try:
            if len(params) == 0:
                pass

            key_name, cipher = params[0], params[1]

            if not self._files.check_key_exist(key_name):
                pass

            key_parts = self._files.get_key(key_name)
            key = {"n": key_parts[0], "exponent": key_parts[1]}
            messageint = self._rsa.decrypt(int(cipher), key)
            message = self._messages.int_to_string(messageint)
            self._pretty_output(f"{message}\n")
        except:
            self._pretty_output("Decryption unsuccesful\n")


    def _help(self, params):
        command = ""

        if len(params) == 0:
            command = " "
        else:
            command = params[0]

        insert = ""
        match command:
            case "generate":
                insert = ("The 'generate' command generates a public-private RSA key pair.\n\n"
                          "Usage:\n"
                          "generate [name]\n\n"
                          "Parameters:\n"
                          "name: Name of the key pair to be generated. Public key will be '[name]_pub'.\n"
                          "      A pre-existing key of the same name will be overwritten.\n")
            case "encrypt":
                insert = ("The 'encrypt' command encrypts/signs a message using the given RSA key.\n\n"
                          "Usage:\n"
                          "encrypt [key] [message]\n\n"
                          "Parameters:\n"
                          "key: Name of the key that will be used for encryption.\n"
                          "message: The message to be encrypted. Multiword messages must be encased with parentheses.\n")
            case "decrypt":
                insert = ("The 'decrypt' command decrypts an encrypted message using the given RSA key.\n"
                          "The key used should be the opposing version to the one used for encryption.\n\n"
                          "Usage:\n"
                          "decrypt [key] [cipher]\n\n"
                          "Parameters:\n"
                          "key: Name of the key that will be used for decryption.\n"
                          "cipher: The encrypted message, which is an integer.\n")
            case "help":
                insert = ("The 'help' command prints information about the given command.\n\n"
                          "Usage:\n"
                          "help [command]\n\n"
                          "Parameters:\n"
                          "command: Name of the command, eg. 'generate'.\n")
            case "exit":
                insert = "Exits the program.\n"
            case " ":
                insert = "The 'help' command requires a command name as a parameter.\n"
            case _:
                insert = f"'{command}' is not a recognized command.\n"

        self._pretty_output(insert)

    def _parse_command(self, command: str):
        parsed_command = shlex.split(command)
        # print(parsed_command)

        return parsed_command

    def _pretty_output(self, output: str):
        print("="*50 +
              f"\n{output}\n" +
              "="*50)

if __name__ == "__main__":
    ui = UI(1)
    ui.start()
