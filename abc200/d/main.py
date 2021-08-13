import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))

is_yes = False
ans_b = None
ans_c = None

n = I()
a = LI()
s = set()
comb = [None for _ in range(200)]

for i in range(n):
  a[i] %= 200

for i in range(1, n+1):
  choices = itertools.combinations(range(n), i)
  for choice in choices:
    total = 0
    for j in choice:
      total += a[j]
    total %= 200
    if total in s:
      is_yes = True
      ans_b = list(comb[total])
      ans_c = list(choice)
      break
    else:
      s.add(total)
      comb[total] = choice
  if is_yes:
    break

if is_yes:
  print('Yes')
  for i in range(len(ans_b)):
    ans_b[i] += 1
  for i in range(len(ans_c)):
    ans_c[i] += 1
  print(len(ans_b), *ans_b)
  print(len(ans_c), *ans_c)
else:
  print('No')
