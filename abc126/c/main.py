import sys
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))

def rec(k, exp):
  if k<=1:
    return
  else:
    exp[:k] = list(map(lambda x: x+1, exp[:k]))
    rec((k+1)//2, exp)

n, k = LI()
exp = [ 0 for _ in range(n+1) ]
rec(k, exp)
exp = list(map(lambda x: ((1/2)**x)/n, exp))
print(round(sum(exp[1:]), 12))