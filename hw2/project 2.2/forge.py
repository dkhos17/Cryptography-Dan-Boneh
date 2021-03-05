import sys
import oracle as orc

BLOCK_SIZE = 16
MAC_BLOCK_SIZE = 2*BLOCK_SIZE

def findMac(msg):

    def macxor(mac, m):
        return bytearray(x[0] ^ x[1] for x in zip(mac, bytearray(m)))

    # mac(m[0]m[1])
    mac = orc.Mac(msg[:MAC_BLOCK_SIZE], MAC_BLOCK_SIZE)
    
    # mac(m[b]m[b+1]m[b+2]m[b+3]) = mac((mac(m[b]m[b+1]) xor m[b+2])m[b+3])
    for b in range(MAC_BLOCK_SIZE, len(msg), MAC_BLOCK_SIZE):
        m1, m2 = msg[b:b+BLOCK_SIZE], msg[b+BLOCK_SIZE:b+MAC_BLOCK_SIZE]
        mac = orc.Mac(macxor(mac, m1) + m2, MAC_BLOCK_SIZE)

    assert orc.Vrfy(msg, len(msg), mac)
    return mac


if __name__ == '__main__':
    assert len(sys.argv) == 2
    with open(sys.argv[1]) as msg:
        orc.Oracle_Connect()
        print(findMac(msg.read()))
        orc.Oracle_Disconnect()
