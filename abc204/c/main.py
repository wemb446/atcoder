import sys
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))

def dfs(num):
  seen[num] = True
  if visited[num]:
    return route[num]

  tmp = list(route[num])
  is_complete = True
  for dist in tmp:
    if seen[dist]:
      if seen[dist]!=visited[dist]:
        is_complete = False
      continue
    route[num] |= dfs(dist)

  if is_complete:
    visited[num] = True
  return route[num]

n, m = LI()
route = [ set() for i in range(n)]
for i in range(m):
  a, b = LI()
  route[a-1].add(b-1)

seen = [False for _ in range(n)]
visited = [False for _ in range(n)]

ans = 0
for i in range(n):
  dfs(i)
  route[i].add(i)
  ans += len(route[i])

print(ans)