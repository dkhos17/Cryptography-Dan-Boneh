key, plaintext = bytes(input(), 'utf-8'), bytes(input(), 'utf-8')

print(bytes([bit^key[i % len(key)] for i, bit in enumerate(plaintext)]).hex())