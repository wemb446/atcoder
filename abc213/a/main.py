import sys
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))

a, b = LI()
print(a^b)