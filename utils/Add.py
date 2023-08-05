from getpass import getpass
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256

from rich import print as printc

from utils.Dbconfig import dbconfig
import utils.AESutil

def computeMasterKey(mp, ds):
    password = mp.encode()
    salt = ds.encode()
    key = PBKDF2(password, salt, 32, count=1000000, hmac_hash_module=SHA256)
    return key

def addEntry(mp, service, password):
    db = dbconfig()
    cursor = db.cursor()
    query = "SELECT device_secret FROM passman.secrets"
    cursor.execute(query)
    res = cursor.fetchall()
    ds = res[0][0]

    mk = computeMasterKey(mp, ds)
    encrypted = utils.AESutil.encrypt(key=mk, source=password, keyType="bytes")

    query = "INSERT INTO passman.entries (service, password) VALUES (%s, %s)"
    val = (service, encrypted)
    cursor.execute(query, val)
    db.commit()
    printc("[green][+][/green] Added entry")


