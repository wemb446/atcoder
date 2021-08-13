import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

n = I()
a = LI()
count_mod = [0 for _ in range(200)]
for i in range(n):
  count_mod[a[i]%200] += 1

ans = 0
for i in range(200):
  if count_mod[i]>=2:
    ans += math.comb(count_mod[i], 2)

print(ans)