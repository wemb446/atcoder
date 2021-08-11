import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))

n = I()
p = LI()
for i in range(n):
  p[i] -= 1

ans = 0
for i in range(n-1):
  if p[i]==i and p[i+1]==i+1:
    p[i], p[i+1] = p[i+1], p[i]
    ans += 1

for i in range(n):
  if p[i]==i:
    ans += 1

print(ans)