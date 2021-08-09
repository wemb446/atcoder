import sys
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))

n, k = LI()
friends = []
for i in range(n):
  a, b = LI()
  friends.append((a, b))
friends.sort(key=lambda x:x[0])

for i in range(n):
  p = friends[i][0]
  if k < p:
    break
  k += friends[i][1]

print(k)