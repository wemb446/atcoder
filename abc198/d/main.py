import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

s1 = S()
s2 = S()
s3 = S()

ss = set()
for c in list(s1)+list(s2)+list(s3):
  ss.add(c)

is_ok = False
n1, n2, n3 = 0, 0, 0
head = [s1[0], s2[0], s3[0]]
dic = {}
chars = list(ss)
for c in chars:
  dic[c] = '0'
c_kinds = len(ss)
if c_kinds <= 10:
  perm_list = itertools.permutations(range(10), c_kinds)
  for l in perm_list:
    s1_, s2_, s3_ = [], [], []
    for i, c in enumerate(chars):
      dic[c] = str(l[i])
    if dic[head[0]]=='0' or dic[head[1]]=='0' or dic[head[2]]=='0':
      continue
    for c in s1:
      s1_.append(dic[c])
    for c in s2:
      s2_.append(dic[c])
    for c in s3:
      s3_.append(dic[c])
    n1 = ''.join(s1_)
    n2 = ''.join(s2_)
    n3 = ''.join(s3_)
    n1_ = int(n1)
    n2_ = int(n2)
    n3_ = int(n3)

    if n1_==0 or n2_==0 or n3_==0:
      continue
    if n1_+n2_==n3_:
      is_ok = True
      break

if is_ok:
  print(n1)
  print(n2)
  print(n3)
else:
  print('UNSOLVABLE')
