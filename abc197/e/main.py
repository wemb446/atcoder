import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

def tol(cx, l, r):
  if cx <= r:
    return r-cx + r-l
  else:
    return cx-l

def tor(cx, l, r):
  if l <= cx:
    return cx-l + r-l
  else:
    return r-cx

n = I()
xc = [LI() for _ in range(n)]
xc.sort(key = lambda x: (x[1], x[0]))

minx = [0, xc[0][0]]
maxx = [0]
for i in range(1, n):
  if xc[i-1][1] != xc[i][1]:
    maxx.append(xc[i-1][0])
    minx.append(xc[i][0])
maxx.append(xc[n-1][0])
minx.append(0)
maxx.append(0)

dp = [ [0, 0] for _ in range(len(minx)) ]
for i in range(1, len(minx)):
  pl, pr = minx[i-1], maxx[i-1]
  cl, cr = minx[i], maxx[i]
  dp[i][0] = min(dp[i-1][0]+tol(pl, cl, cr), dp[i-1][1]+tol(pr, cl, cr))
  dp[i][1] = min(dp[i-1][0]+tor(pl, cl, cr), dp[i-1][1]+tor(pr, cl, cr))
print(min(dp[-1][0], dp[-1][1]))
