import sys
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()

n, k = LI()
s = S()

s = s[:k-1] + s[k-1].lower() + ( s[k:] if k != n else '' )
print(s)