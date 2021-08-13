import bisect, collections, copy, heapq, itertools, math, string
import sys
sys.setrecursionlimit(1000000)

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

n = I()
c = LI()
route = [ [] for _ in range(n) ]
for _ in range(n-1):
  a, b = LI()
  a -= 1
  b -= 1
  route[a].append(b)
  route[b].append(a)

for i in range(n):
  route[i].sort()

ans = []
color = dict()
for i in range(1000000):
  color[i] = 0
visited = set()
def dfs(current_node):
  visited.add(current_node)

  if color[c[current_node]]==0:
    ans.append(current_node+1)
  color[c[current_node]] += 1
  
  for next in route[current_node]:
    if next in visited:
      continue
    dfs(next)
  
  color[c[current_node]] -= 1

dfs(0)
ans.sort()
for node in ans:
  print(node)