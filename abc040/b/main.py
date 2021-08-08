import math
n = int(input())
H = int(math.sqrt(n))

ans = 100000
for h in range(1, H+1):
  w = n//h
  ref = abs(w-h) + (n-h*w)
  if ref < ans:
    ans = ref

print(ans)