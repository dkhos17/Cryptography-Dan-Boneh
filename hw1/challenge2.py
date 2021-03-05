hex1, hex2 = input(), input()
print(''.join([hex(int(h[0], 16)^int(h[1], 16))[2:] for h in zip(hex1,hex2)]))