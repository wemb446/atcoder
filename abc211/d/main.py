import sys, queue
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))

n, m = LI()
route = [ [] for _ in range(n) ]
seen = [ False for _ in range(n) ]
goto = queue.Queue()
dp = [ {'cost':n, 'count':0} for _ in range(n) ]  # [移動コスト(n=inf), 同コストでの経路数

for i in range(m):
  a, b = LI()
  a -= 1
  b -= 1
  route[a].append(b)
  route[b].append(a)

# 初期条件
seen[0] = True
goto.put(0)
dp[0]['cost'] = 0
dp[0]['count'] = 1
while not goto.empty():
  current = goto.get()
  for next in route[current]:
    if not seen[next]:
      seen[next] = True
      goto.put(next)
    
    if dp[current]['cost']+1 < dp[next]['cost']:
      dp[next]['cost'] = dp[current]['cost']+1
      dp[next]['count'] = dp[current]['count']
    elif dp[current]['cost']+1 == dp[next]['cost']:
      dp[next]['count'] += dp[current]['count']
      dp[next]['count'] %= 1000000007

print(0 if dp[n-1]['cost']==n else dp[n-1]['count'])