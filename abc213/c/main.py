import sys
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))

h, w, n = LI()
a, b = [], []
for i in range(n):
  a_, b_ = LI()
  a.append(a_)
  b.append(b_)

sorted_a = sorted(enumerate(a), key=lambda x:x[1])
sorted_b = sorted(enumerate(b), key=lambda x:x[1])

print(sorted_a, sorted_b)

count_a = 0
count_b = 0
for i in range(n):
  if i>0:
    if sorted_a[i-1][1]==sorted_a[i][1]:
      count_a += 1
    if sorted_b[i-1][1]==sorted_b[i][1]:
      count_b += 1
  print(sorted_a[i][0]+1-count_a, sorted_b[i][0]+1-count_b)