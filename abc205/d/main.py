import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))

def binary_search(arr, num, left, right):
  if right-left<=1:
    return left
  mid = (left+right)//2
  ref = arr[mid]
  if num < ref:
    return binary_search(arr, num, left, mid)
  else:
    return binary_search(arr, num, mid, right)

n, q = LI()
a = LI()
for i in range(q):
  k = I()
  index = binary_search(a, k, 0, n-1)
  ans = k + index
  if index==0 and k<a[0]:
    j=-1
  else:
    j = index
    ans += 1
  if j<n-1 and a[j+1]<=ans:
    ans += 1
    j += 1
  print(ans)