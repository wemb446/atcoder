import sys
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))

a, b, c = LI()

if c%2==0:
  c = 2
else:
  c = 3

a_ = pow(a, c)
b_ = pow(b, c)

ans = ''
if a_ < b_:
  ans = '<'
elif a_ > b_:
  ans = '>'
else:
  ans = '='
print(ans)