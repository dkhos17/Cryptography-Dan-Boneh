import math
import oracle as orc
import helper as hlp

# RSA key (decimal)
N = 119077393994976313358209514872004186781083638474007212865571534799455802984783764695504518716476645854434703350542987348935664430222174597252144205891641172082602942313168180100366024600206994820541840725743590501646516068078269875871068596540116450747659687492528762004294694507524718065820838211568885027869
# public exponent (decimal)
e = 65537L

class MODN:
  def __init__(self, mod):
    self.mod = mod
    self.pows = {}

  def pow(self, x, y):
    if (x,y) not in self.pows:
      self.pows[(x,y)] = pow(x, y, self.mod)
    return self.pows[(x,y)]

  def rev(self, x):
    a, b, p = 1, 0, self.mod
    while x > 1: 
      q, p, x = x // p, x % p, p 
      a, b = b, a - q*b 
    return (a + self.mod) % self.mod

  def mul(self, x, y):
	  return (x * y) % self.mod

  def div(self, x, y):
	  return self.mul(x, self.rev(y))
  
  def add(self, x, y):
    return (x + y) % self.mod 


def findSign(msg):
    M, MOD = hlp.ascii_to_int(MSG), MODN(N)
    
    def splitM(M):
        for M1 in reversed(range(2, 1 << 20)): # should be sqrt(M), but too large...
            if M % M1 == 0: return 1, M1, M/M1
        print "too large M to split."
        return 1, math.sqrt(M), math.sqrt(M)
    
    M0, M1, M2 = splitM(M)
    S0, S1, S2 = orc.Sign(M0), orc.Sign(M1), orc.Sign(M2)
    S = MOD.div(MOD.mul(S1, S2), S0)
    return M, S

def verifySign(MS):
    assert orc.Verify(MS[0], MS[1])
    return MS[1]

if __name__ == '__main__':
    orc.Oracle_Connect()
    MSG = "Crypto is hard --- even schemes that look complex can be broken"
    print verifySign(findSign(MSG))
    orc.Oracle_Disconnect()