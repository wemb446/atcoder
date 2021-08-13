import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

n = I()
if n==0:
  n=1
while n%10==0:
  n //= 10

n_list = []
while n>0:
  n_list.append(n%10)
  n //= 10

n_len = len(n_list)
is_ok = True
for i in range(n_len//2):
  if n_list[i] != n_list[n_len-1-i]:
    is_ok = False
    break

print('Yes' if is_ok else 'No')