import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))

n = I()
a = LI()
b = LI()
c = LI()

set_a = set(a)
count_a = {}
for num in set_a:
  count_a[num] = 0
for num in a:
  count_a[num] += 1

count_b = {}
for num in set(b):
  count_b[num] = 0
for i in range(n):
  count_b[b[c[i]-1]] += 1

ans = 0
for k, v in count_b.items():
  if v==0:
    continue
  if k in set_a:
    ans += count_a[k]*v

print(ans)