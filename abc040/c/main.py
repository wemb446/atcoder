n = int(input())
a = list(map(int, input().split()))
dp = [1000000000 for _ in range(n)]
dp[0] = 0
for i in range(n-1):
  if dp[i]+abs(a[i]-a[i+1]) < dp[i+1]:
    dp[i+1] = dp[i]+abs(a[i]-a[i+1])
  if i < n-2 and dp[i]+abs(a[i]-a[i+2]) < dp[i+2]:
    dp[i+2] = dp[i]+abs(a[i]-a[i+2])
print(dp[-1])