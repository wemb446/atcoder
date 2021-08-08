import sys
def I(): return int(sys.stdin.readline().rstrip())
n = I()
price = n*1.08//1
if price<206:
  print('Yay!')
elif price==206:
  print('so-so')
else:
  print(':(')