import sys
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))

a, b, c = LI()
print( "YES" if b-a==c-b else "NO" )