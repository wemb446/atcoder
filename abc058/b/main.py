import sys
def S(): return sys.stdin.readline().rstrip()

o = S()
e = S()
i = 0
ans = []
while i<len(o):
  ans.append(o[i])
  if i<len(e):
    ans.append(e[i])
  i += 1
print("".join(ans))