import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))

n = I()
a = LI()

ans = 0
for i in range(n):
  ans += a[i] - 10 if 10 < a[i] else 0

print(ans)