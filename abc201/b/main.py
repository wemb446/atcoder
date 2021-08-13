import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

n = I()
input_list = []
for i in range(n):
  s, t = LS()
  input_list.append((s, int(t)))
input_list.sort(key=lambda x:x[1], reverse=True)
print(input_list[1][0])
