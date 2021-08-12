import sys
def I(): return int(sys.stdin.readline().rstrip())
def S(): return sys.stdin.readline().rstrip()

n = I()
a = [S() for _ in range(n)]
INF = 99

count_ans = {}
count_template = {}
for i in range(ord('a'), ord('z')+1):
  count_ans[chr(i)] = INF
  count_template[chr(i)] = 0

for i in range(n):
  count = count_template.copy()
  for c in a[i]:
    count[c] += 1
  for key in count_ans.keys():
    count_ans[key] = min(count_ans[key], count[key])

ans = []
for key in count_ans.keys():
  if count_ans[key]<INF:
    ans.append(key*count_ans[key])
print("".join(ans))