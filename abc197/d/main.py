import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

n = I()
x0, y0 = LI()
xh, yh = LI()
xo, yo = (x0+xh)/2, (y0+yh)/2

x0 -= xo
y0 -= yo
r = math.sqrt( x0*x0 + y0*y0 )
rad0 = math.atan2(y0, x0)
rad1 = rad0 + 2*math.pi/n
x1 = r*math.cos(rad1) + xo
y1 = r*math.sin(rad1) + yo
print(x1, y1)