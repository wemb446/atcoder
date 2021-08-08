n = int(input())
arr = []
for i in range(n):
  t, l, r = map(int, input().split())
  if t==2:
    r -= 0.5
  elif t==3:
    l += 0.5
  elif t==4:
    l += 0.5
    r -= 0.5
  arr.append([l, r])
arr = sorted(arr, key=lambda x: x[1])

count = 0
for i in range(n):
  for j in range(i+1, n):
    if arr[j][0] <= arr[i][1]:
      count += 1
print(count)
