import shlex

class UI:
    def __init__(self, rsa_handler, file_handler, message_handler):
        self._rsa = rsa_handler
        self._files = file_handler
        self._messages = message_handler

    def start(self):
        while True:
            print("RSA tool running, enter command:\n\n"
                  f"{'generate':15}{'[name]':15}{'[path]':15}\n"
                  f"{'encrypt':15}{'[key]':15}{'[message]':15}\n"
                  f"{'decrypt':15}{'[key]':15}{'[message]':15}\n"
                  f"{'help':15}{'[command]':15}\n"
                  f"exit")
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

    def _encrypt(self, params):
        if len(params) == 0:
            pass

        key_name, message = params[0], params[1]

        if not self._files.check_key_exist(key_name):
            pass

        messageint = self._messages.string_to_int(message)

        key_parts = self._files.get_key(key_name)
        key = {"n": key_parts[0], "exponent": key_parts[1]}
        cipher = self._rsa.encrypt(messageint, key)
        print(cipher)

    def _decrypt(self, params):
        if len(params) == 0:
            pass

        key_name, cipher = params[0], params[1]

        if not self._files.check_key_exist(key_name):
            pass

        key_parts = self._files.get_key(key_name)
        key = {"n": key_parts[0], "exponent": key_parts[1]}
        messageint = self._rsa.decrypt(int(cipher), key)
        message = self._messages.int_to_string(messageint)
        print(message)

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
                          "generate [name] [path]\n\n"
                          "Parameters:\n"
                          "name: Name of the key pair to be generated\n"
                          "path: Path to the directory the key pair will be stored in. If not specified, defaults to x.\n")
            case "encrypt":
                insert = ""
            case "decrypt":
                insert = ""
            case "help":
                insert = ("The 'help' command prints information about the given command.\n\n"
                          "Usage:\n"
                          "help [command]\n\n"
                          "Parameters:\n"
                          "command: Name of the command, eg. 'generate'\n")
            case "exit":
                insert = "Exits the program."
            case " ":
                insert = "The 'help' command requires a command name as a parameter.\n"
            case _:
                insert = f"'{command}' is not a recognized command.\n"

        print("="*50 +
              f"\n{insert}\n" +
              "="*50)

    def _parse_command(self, command: str):

        # Separate arguments by whitespaces
        """
        parsed_command = []
        param_start_i, param_end_i = 0, 0
        in_quotes, escaping_quotes, last_bad = False , False, False
        for i in range(len(command)):
            param_end_i = i
            if in_quotes:
                if command[i] == '"' and not escaping_quotes:
                    parsed_command.append(command[param_start_i:param_end_i])
                    in_quotes = False
                    continue
                elif command[i] == "\\":
                    escaping_quotes = True
                else:
                    param_end_i = i

            else:
                if command[i] == " ":
                    if last_bad:
                        continue
                    parsed_command.append(command[param_start_i:param_end_i])
                    last_bad = True
        """
        parsed_command = shlex.split(command)
        print(parsed_command)

        return parsed_command


if __name__ == "__main__":
    ui = UI(1)
    ui.start()
