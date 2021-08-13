import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

r, x, y = LI()
dist = math.sqrt(x*x+y*y)
ans = dist//r
if dist%r==0:
  ans = ans
elif ans==0:
  ans = 2
else:
  ans += 1
print(int(ans))