import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

n = I()
a = LI()
s = [ [0]*n for _ in range(n) ]
for i in range(n):
  s[i][i] = a[i]
  for j in range(i+1, n):
    s[i][j] = s[i][j-1]|a[j]

ans = float('inf')
for i in range(n):
  combs = itertools.combinations(range(n-1), i)
  for comb in combs:
    l = list(comb)
    l.append(n-1)
    
    xor = 0
    i = 0
    for j in l:
      xor ^= s[i][j]
      i = j+1
    if xor < ans:
      ans = xor

print(ans)
