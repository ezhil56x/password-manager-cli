import hashlib
from utils.Dbconfig import dbconfig


def verifyMasterPassword(mp):
    db = dbconfig()
    cursor = db.cursor()

    query = "SELECT masterkey_hash FROM passman.secrets"
    cursor.execute(query)
    res = cursor.fetchall()

    hashed_mp = hashlib.sha256(mp.encode()).hexdigest()

    if hashed_mp==res[0][0]:
        return True
    else:
        return False