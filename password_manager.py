import sys

import pyperclip
from lib.Argument import Argument
from utils.Add import addEntry
from utils.Retrieve import retrieveEntries
from utils.Verifymp import verifyMasterPassword
from utils.GeneratePassword import generate_password
from utils.Config import config

from rich import print as printc

parser = Argument()
args = sys.argv

parser.parse_args(args)

if parser.option == ['--help']:
    parser.print_help()
    sys.exit(0)

if parser.option == ['--config']:
  config()
  sys.exit(0)

if '--operation' in parser.option:
    try:
        operation = parser.optionValues['--operation']
    except KeyError:
        print("Missing --operation argument, use --help for help")
        sys.exit(0)
else:
    print("Missing --operation argument, use --help for help")
    sys.exit(0)

if operation=="store":
    if '--operation' not in parser.option or '--master-password' not in parser.option or '--service' not in parser.option or '--password' not in parser.option:
        print("Usage: python3 password_manager.py --operation store --master-password <master-password> --service <service> --password <password>")
        sys.exit(0)
    masterPassword = parser.optionValues['--master-password']
    service = parser.optionValues['--service']
    password = parser.optionValues['--password']
    if (verifyMasterPassword(masterPassword)==True):
        addEntry(masterPassword, service, password)
        sys.exit(0)
    else:
        printc("[red][-] Master password is incorrect, try again![/red]")

if operation=="retrieve":
    if '--operation' not in parser.option or '--master-password' not in parser.option or '--search' not in parser.option:
        print("Usage: python3 password_manager.py --operation retrieve --master-password <master-password> --search <search>")
        sys.exit(0)
    masterPassword = parser.optionValues['--master-password']
    search = parser.optionValues['--search']
    if (verifyMasterPassword(masterPassword)):
        retrieveEntries(masterPassword, search=search)
        sys.exit(0)
    else:
        printc("[red][-] Master password is incorrect, try again![/red]")

if operation=="generate":
    if '--length' in parser.option:
        try:
            try:
                if parser.optionValues['--length'].isdigit:
                    length = parser.optionValues['--length']
                    gpasswd = generate_password(int(length))
                    pyperclip.copy(gpasswd)
                    print('----------------------------------')
                    printc("[green][+][/green] This is your generated password: " + gpasswd)
                    printc("[green][+][/green] Password copied to clipboard")
                    print('----------------------------------')
                    sys.exit(0)
            except ValueError:
                printc("[red][-] Length must be an integer [/red]")
        except KeyError:
            printc("[red][-] Length value is missing [/red]")
    else:
        print("Usage: python3 password_manager.py --operation generate --length <length>")


