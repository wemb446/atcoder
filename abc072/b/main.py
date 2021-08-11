import sys
def S(): return sys.stdin.readline().rstrip()

s = list(S())
ans = []
for i in range(0, len(s), 2):
  ans.append(s[i])
print(''.join(ans))