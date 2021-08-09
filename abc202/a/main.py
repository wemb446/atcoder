import sys
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
print(21-sum(LI()))