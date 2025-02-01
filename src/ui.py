class UI:
    def __init__(self, rsa_handler):
        self.rsa = rsa_handler

    def start(self):
        while True:
            print("RSA tool running, enter command:\n\n"
                  f"{'generate':15}{'[name]':15}{'[path]':15}\n"
                  f"{'encrypt':15}{'[message]':15}{'[key_path]':15}\n"
                  f"{'decrypt':15}{'[message]':15}{'[key_path]':15}\n"
                  f"{'help':15}{'[command]':15}\n"
                  f"exit")
            user_input = self._parse_command(input("> "))
            command, params = user_input[0], user_input[1:]

            match command:
                case "generate":
                    pass
                case "encrypt":
                    pass
                case "decrypt":
                    pass
                case "help":
                    self._help(params)
                case "exit":
                    print("Exiting...")
                    break

    def _help(self, params):
        command = ""

        if len(params) == 0:
            command = " "
        else:
            command = params[0]

        insert = ""
        match command:
            case "generate":
                insert = (f"The 'generate' command generates a public-private RSA key pair.\n\n"
                          f"Usage:\n"
                          f"generate [name] [path]\n\n"
                          f"Parameters:\n"
                          f"name: Name of the key pair to be generated\n"
                          f"path: Path to the directory the key pair will be stored in. If not specified, defaults to x.\n")
            case "encrypt":
                insert = ""
            case "decrypt":
                insert = ""
            case "help":
                insert = (f"The 'help' command prints information about the given command.\n\n"
                          f"Usage:\n"
                          f"help [command]\n\n"
                          f"Parameters:\n"
                          f"command: Name of the command, eg. 'generate'\n")
            case "exit":
                insert = ""
            case " ":
                insert = f"The 'help' command requires a command name as a parameter.\n"
            case _:
                insert = f"'{command}' is not a recognized command.\n"

        print("="*50 +
              f"\n{insert}\n" +
              "="*50)

    def _parse_command(self, command: str):

        # Separate arguments by whitespaces
        parsed_command = command.split(" ")

        # Purge all accidental excess whitespaces
        parsed_command = [param for param in parsed_command if param != ""]

        return parsed_command


if __name__ == "__main__":
    ui = UI(1)
    ui.start()
