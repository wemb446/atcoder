import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))

n = I()
a = set(LI())

if len(a)==n:
  print('Yes')
else:
  print('No')