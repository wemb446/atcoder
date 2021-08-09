import sys
def S(): return sys.stdin.readline().rstrip()

s = S()
ans = []
for c in reversed(list(s)):
  if c=='6':
    c = '9'
  elif c=='9':
    c = '6'
  ans.append(c)
print(''.join(ans))