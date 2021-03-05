import math

class MODP:
  def __init__(self, mod):
    self.mod = mod
    self.pows = {}

  def pow(self, x, y):
    if (x,y) not in self.pows:
      self.pows[(x,y)] = pow(x, y, self.mod)
    return self.pows[(x,y)]

  def rev(self, x):
    return self.pow(x, self.mod-2)

  def mul(self, x, y):
	  return (x * y) % self.mod

  def div(self, x, y):
	  return self.mul(x, self.rev(y))
  
  def add(self, x, y):
    return (x + y) % self.mod
	
  def dis_log(self, h, g, x0, x1, B):
    # x = x0*B + x1
    x = self.add(self.mul(x0, B),  x1)
    # check if h = g^x (mod p) 
    assert h == self.pow(g, x)
    return x

# Find x such that g^x = h (mod p)
# 0 <= x <= max_x
def discrete_log(g, h, p, max_x):
  B, MOD, X1 = int(math.sqrt(max_x)), MODP(p), {}

  key = MOD.div(h,1) # h/g^0
  for x1 in range(0,B):
	  X1[key] = x1
	  key = MOD.div(key,g) # h/g^x1

  key = 1 # (g^B)^0
  for x0 in range(0,B):
    if key in X1:
        return MOD.dis_log(h, g, x0 ,X1[key], B)
    key = MOD.mul(key, MOD.pow(g,B)) # (g^B)^x0
  
  return -1


def main():
	p = 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171
	g = 11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568
	h = 3239475104050450443565264378728065788649097520952449527834792452971981976143292558073856937958553180532878928001494706097394108577585732452307673444020333
	max_x = 1 << 40 # 2^40
	print discrete_log(g, h, p, max_x)

if __name__ == '__main__':
	main()

