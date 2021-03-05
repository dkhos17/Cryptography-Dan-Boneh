from base64 import b64encode, b64decode

hex = input()
print(b64encode(bytes.fromhex(hex)).decode())