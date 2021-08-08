import sys
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))

x, y = LI()
if x==y:
  print(x)
else:
  print(3-x-y)