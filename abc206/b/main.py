import sys
def I(): return int(sys.stdin.readline().rstrip())
n = I()

i = 0
total = 0
while total<n:
  i += 1
  total += i
print(i)