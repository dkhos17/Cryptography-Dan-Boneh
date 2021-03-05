import sys
import oracle as orc

ASCII = 256
BLOCK_SIZE = 16

def decipher(cmsg):
    CMSG = bytearray((int(cmsg[i:i+2], BLOCK_SIZE)) for i in range(0, len(cmsg), 2))
    PADDING = {b : ([0]*(BLOCK_SIZE - b) + [b]*b) for b in range(1, BLOCK_SIZE+1)}

    DECIPHERED = []
    while len(CMSG) >= 2*BLOCK_SIZE:
        BLOCK = [0] * BLOCK_SIZE
        for b in range(1, BLOCK_SIZE+1):
            for x in range(ASCII):
                BLOCK[-b] = x
                if x == b: continue
                
                tryX = CMSG[:]
                for i in range(BLOCK_SIZE):
                    tryX[-2*BLOCK_SIZE + i] ^= BLOCK[i] ^ PADDING[b][i]

                if orc.Oracle_Send(tryX, len(tryX) / BLOCK_SIZE):
                    break
            else:
                BLOCK[-b] = b

        CMSG, DECIPHERED = CMSG[:-BLOCK_SIZE], BLOCK + DECIPHERED
    
    return bytearray(DECIPHERED[:-DECIPHERED[-1]])


if __name__ == '__main__':
    assert len(sys.argv) == 2
    with open(sys.argv[1]) as cyp:
        orc.Oracle_Connect()
        print(decipher(cyp.read()))
        orc.Oracle_Disconnect()
