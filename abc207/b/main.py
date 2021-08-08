a, b, c, d = map(int, input().split())
if a+b-c*d <= a+2*b-2*c*d:
  ans = -1
else:
  i = 0
  while a+i*b>i*c*d:
    i += 1
  ans = i
print(ans) 