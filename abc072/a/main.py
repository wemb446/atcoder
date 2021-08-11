import sys
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))

x, t = LI()
if x<t:
  ans = 0
else:
  ans = x-t
print(ans)