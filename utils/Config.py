import sys
from utils.Dbconfig import dbconfig
from rich import print as printc
from rich.console import Console
import hashlib
import random
import string

from getpass import getpass

console = Console()

def generateDeviceSecret(length=10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def config():
    db = dbconfig()
    cursor = db.cursor()

    try:
        cursor.execute("CREATE DATABASE passman")
    except Exception as e:
        console.print_exception(show_locals=True)
        sys.exit(0)
    printc("[green][+][/green] Database 'passman' created")


    query = "CREATE TABLE passman.secrets (masterkey_hash TEXT NOT NULL, device_secret TEXT NOT NULL)"
    res = cursor.execute(query)
    printc("[green][+][/green] Table 'secrets' created")

    query = "CREATE TABLE passman.entries (service TEXT NOT NULL, password TEXT NOT NULL)"
    res = cursor.execute(query)
    printc("[green][+][/green] Table 'entries' created")
    printc("--------------------------")

    while 1:
        mp = getpass("Enter master password: ")
        if mp==getpass("Confirm master password: ") and mp!="":
            break
        printc("[red][-] Passwords do not match, try again [/red]")
    printc("--------------------------")

    hashed_mp = hashlib.sha256(mp.encode()).hexdigest()
    printc("[green][+][/green] Generated hash of master password")

    ds = generateDeviceSecret()

    query = "INSERT INTO passman.secrets (masterkey_hash, device_secret) VALUES (%s, %s)"
    val = (hashed_mp, ds)
    cursor.execute(query, val)

    db.commit()

    printc("[green][+][/green] Added to the database")
    printc("[green][+][/green] Configuration done!")
    printc("--------------------------")
    printc("[yellow][!][/yellow] Use --help to see available options")
    db.close()


