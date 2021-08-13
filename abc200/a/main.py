import sys
def I(): return int(sys.stdin.readline().rstrip())
n = I()
print((n-1)//100+1)