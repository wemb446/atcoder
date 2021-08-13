import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

h, w, x, y = LI()
s = [S() for _ in range(h)]

ans = 1 

i = y-1
while i+1<w and s[x-1][i+1]!='#':
  ans += 1
  i += 1

i = y-1
while 0<=i-1 and s[x-1][i-1]!='#':
  ans += 1
  i -= 1

i = x-1
while i+1<h and s[i+1][y-1]!='#':
  ans += 1
  i += 1

i= x-1
while 0<=i-1 and s[i-1][y-1]!='#':
  ans += 1
  i -= 1

print(ans)
