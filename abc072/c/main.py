import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))

n = I()
a = sorted(LI())
ans, count_previous2, count_previous, count_current = 0, 0, 0, 0
if n==1:
  ans = 1
for i in range(len(a)):
  count_current += 1
  ans = max(ans, count_previous2+count_previous+count_current)
  if i < len(a)-1 and a[i] != a[i+1]:
    if a[i]+2 < a[i+1]:
      count_previous2, count_previous, count_current = 0, 0, 0
    elif a[i]+2 == a[i+1]:
      count_previous2, count_previous, count_current = count_current, 0, 0
    elif a[i]+1 == a[i+1]:
      count_previous2, count_previous, count_current = count_previous, count_current, 0
print(ans)