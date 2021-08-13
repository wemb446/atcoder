import sys
def S(): return list(sys.stdin.readline().rstrip())

s = S()
count = {
  "o": 0,
  "x": 0,
  "?": 0,
}
for c in s:
  count[c] += 1

ans = 0
  

