
n,k =map(int,input().split())
dp = [0]*1001
dp[0]=1
#n!/n-k! k!
for i in range(n+1):
  if dp[i]:
    continue
  else:
    dp[i]=i*dp[i-1]

print((dp[n]//(dp[n-k]*dp[k]))%10007)
