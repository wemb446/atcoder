import sys
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
a = LI()
a.sort()
print("Yes" if a[2]-a[1]==a[1]-a[0] else "No")