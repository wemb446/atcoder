import sys
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))

a, b = LI()
ans = a*b/100
print(ans)