
import base64
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
import sys

def encrypt(key, source, encode=True, keyType = 'hex'):
	source = source.encode()
	if keyType == "hex":
		key = bytes(bytearray.fromhex(key))

	IV = Random.new().read(AES.block_size)
	encryptor = AES.new(key, AES.MODE_CBC, IV)
	padding = AES.block_size - len(source) % AES.block_size
	source += bytes([padding]) * padding
	data = IV + encryptor.encrypt(source)
	return base64.b64encode(data).decode() if encode else data


def decrypt(key, source, decode=True,keyType="hex"):
	source = source.encode()
	if decode:
		source = base64.b64decode(source)

	if keyType == "hex":
		key = bytes(bytearray.fromhex(key))

	IV = source[:AES.block_size]
	decryptor = AES.new(key, AES.MODE_CBC, IV)
	data = decryptor.decrypt(source[AES.block_size:])
	padding = data[-1]
	if data[-padding:] != bytes([padding]) * padding:
		raise ValueError("Invalid padding...")
	return data[:-padding]