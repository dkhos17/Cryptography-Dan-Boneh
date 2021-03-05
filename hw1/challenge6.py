from base64 import b64encode, b64decode

def hamming_distance(str1, str2):
    if len(str1) != len(str2): return 0
    return sum([bin(bytes[0]^bytes[1]).count('1') for bytes in zip(bytes(str1, 'utf-8'), bytes(str2, 'utf-8'))])

assert(hamming_distance('this is a test', 'wokka wokka!!!') == 37)

def score(s, keysize):
    chunks = [s[i:i+keysize] for i in range(0, len(s), keysize)]
    return sum([hamming_distance(chunks[i], chunks[i+1]) / keysize for i in range(len(chunks)-2)]) / len(chunks)

def find_keysize(s):
    return min([(score(s, keysize), keysize) for keysize in range(2,41)])[1]   

hex = b64decode(input()).decode('utf-8')
KEYSIZE = find_keysize(hex)
# print(KEYSIZE)

blocks = {}
for i, b in enumerate(hex):
    if i % KEYSIZE in blocks:
        blocks[i % KEYSIZE] += b
    else:
        blocks[i % KEYSIZE] = b

# print(blocks)

# --- from challange 3 --- # 
scores = {'a': 0.0651738,'b': 0.0124248,'c': 0.0217339,'d': 0.0349835,'e': 0.1041442,'f': 0.0197881,'g': 0.0158610,'h':   0.0492888,'i': 0.0558094,'j': 0.0009033,'k': 0.0050529,'l': 0.0331490,'m': 0.0202124,'n': 0.0564513,'o':                 0.0596302,'p': 0.0137645,'q': 0.0008606,'r': 0.0497563,'s': 0.0515760,'t': 0.0729357,'u': 0.0225134,'v':                 0.0082903,'w': 0.0171272,'x': 0.0013692,'y': 0.0145984,'z': 0.0007836,' ': 0.1918182}

def decodeBy(key, block):
    return ''.join(chr(ord(b)^key) for b in block)

def total_score(key, block):
    score = 0.0
    for c in decodeBy(key, block):
        if c.lower() in scores:
            score += scores[c.lower()]
    return score
            
def findKey(block):
    return max([(total_score(key, block), key) for key in range(256)])[1]     

key = ''.join([chr(findKey(block)) for block in blocks.values()])
# print(key)

# --- from challange 5 --- # 
print(''.join([chr(ord(bit)^ord(key[i % len(key)])) for i, bit in enumerate(hex)]))