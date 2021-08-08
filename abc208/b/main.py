p = int(input())

coin = []
num = 1
for i in range(1, 11):
  num *= i
  coin.append(num)

count = 0
for i in range(9, -1, -1):
  while coin[i] <= p:
    p -= coin[i]
    count += 1

print(count)