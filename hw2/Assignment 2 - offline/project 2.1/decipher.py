import sys
import oracle as orc

def decipher(txt):



    return txt



if __name__ == '__main__':
    assert len(sys.argv) == 2
    with open(sys.argv[1]) as cyp:
        orc.Oracle_Connect()
        print(decipher(cyp.read()))
        orc.Oracle_Disconnect()
