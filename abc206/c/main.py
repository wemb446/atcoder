import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))

n = I()
a = LI()
count = dict()
ans = 0
for i, num in enumerate(a):
  if num not in count.keys():
    count[num] = 1
  else:
    count[num] += 1
  ans += i+1 - count[num]
print(ans)