import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

n = I()
s = list(S())
q = I()
is_swap = False

for _ in range(q):
  t, a, b = LI()
  if t==1:
    if is_swap:
      a = (a+n)%(2*n)
      b = (b+n)%(2*n)
    s[a-1], s[b-1] = s[b-1], s[a-1]
  else:
    is_swap = not is_swap

if is_swap:
  s = s[n:] + s[:n]

print(''.join(s))