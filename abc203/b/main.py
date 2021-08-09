import sys
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))

n, k = LI()
print((n*(n+1)//2)*k*100+(k*(k+1)//2)*n)