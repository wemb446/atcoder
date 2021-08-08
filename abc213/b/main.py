import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))

n = I()
a = LI()

dic = {}
for i, num in enumerate(a):
  dic[i] = num
dic_sorted = sorted(dic.items(), key=lambda x:x[1])

print(dic_sorted[-2][0]+1)