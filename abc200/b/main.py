import sys
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
n, k = LI()
for _ in range(k):
  n = n//200 if n%200==0 else n*1000+200
print(n)