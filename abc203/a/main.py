import sys
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))

a, b, c = LI()
ans = 0
if a==b:
  ans = c
elif b==c:
  ans = a
elif c==a:
  ans = b
print(ans)