import sys
def S(): return sys.stdin.readline().rstrip()

s = S()
s1, s2 = int(s[:2]), int(s[2:])
q1 = 1 <= s1 <= 12
q2 = 1 <= s2 <= 12

if q1 and q2:
  print('AMBIGUOUS')
elif q1:
  print('MMYY')
elif q2:
  print('YYMM')
else:
  print('NA')