import sys
sys.setrecursionlimit(1000000)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))

def dfs(num):
  seen.add(num)
  visited.append(num+1)
  for next in route[num]:
    if next in seen:
      continue
    dfs(next)
    visited.append(num+1)
  return


n = I()
route = [[] for _ in range(n)]
for i in range(n-1):
  a, b = LI()
  a -= 1
  b -= 1
  route[a].append(b)
  route[b].append(a)

for i in range(n):
  route[i].sort()

visited = []
seen = set()
dfs(0)

print(*visited)