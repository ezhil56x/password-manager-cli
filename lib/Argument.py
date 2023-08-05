class Argument:
    def __init__ (self):
        self.option = []
        self.optionValues = {}

    def parse_args(self, args):
        for arg in args:
            if arg.startswith('--'):
                self.option.append(arg)
                if args.index(arg) + 1 < len(args):
                    self.optionValues[arg] = args[args.index(arg) + 1]

    def print_help(self):
        print("Usage: python3 password_manager.py --operation <operation> --master-password <master-password> [--service <service> --password <password>] [--search <search>]\n")
        print("Options:")
        print("\t--help: Print this help message")
        print("\t--config: Configure the database and master password (Use this only once after installation)")
        print("\t--operation: Choose the operation to perform (store, retrieve, generate)")
        print("\t--master-password: The main password to access all the stored passwords")
        print("\t--service: The service for which the password is to be stored like 'facebook', 'gmail', etc (Required for storing passwords)")
        print("\t--password: The password to be stored for the service (Required for storing passwords)")
        print("\t--search: Search for a service and retrieve its password (Required for retrieving passwords)")
        print("\t--length: Length of the password to be generated (Required for generating passwords)")

