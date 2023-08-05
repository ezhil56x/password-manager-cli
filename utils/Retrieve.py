from utils.Dbconfig import dbconfig
from rich import print as printc
from rich.table import Table
from rich.console import Console

import pyperclip

import utils.AESutil

from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256

def computeMasterKey(mp, ds):
    password = mp.encode()
    salt = ds.encode()
    key = PBKDF2(password, salt, 32, count=1000000, hmac_hash_module=SHA256)
    return key

def retrieveEntries(mp, search):
    db = dbconfig()
    cursor = db.cursor()

    query = "SELECT device_secret FROM passman.secrets"
    cursor.execute(query)
    res = cursor.fetchall()
    ds = res[0][0]

    query = "SELECT * FROM passman.entries WHERE service LIKE '%{}%'".format(search)

    cursor.execute(query)
    res = cursor.fetchall()

    if len(res)==0:
        printc("[yellow][-][/yellow] No entries found")
        return
    
    if len(res)==1:
        mk = computeMasterKey(mp, ds)
        decrypted = utils.AESutil.decrypt(key=mk, source=res[0][1], keyType="bytes")
        pyperclip.copy(decrypted.decode())
        printc("[green][+][/green] Password found for service", res[0][0])
        printc("[green][+][/green] Password copied to clipboard")

    if len(res)>1:
        table = Table(title="Results")
        table.add_column("Service")
        table.add_column("Password")

        for i in res:
            mk = computeMasterKey(mp, ds)
            decrypted = utils.AESutil.decrypt(key=mk, source=i[1], keyType="bytes")
            table.add_row(i[0], decrypted.decode())
        console = Console()
        console.print(table)

        return

    db.close()