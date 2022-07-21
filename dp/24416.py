
def fibo_recur(n):
    global cnt_recur
    if n==1 or n==2:
        return 1
    else:
        cnt_recur += 1
        return fibo_recur(n-1)+fibo_recur(n-2)

def fibo_dp(n):
    global cnt_dp
    if not dp[n]:
        cnt_dp += 1
        dp[n]=fibo_dp(n-1)+fibo_dp(n-2)
    return dp[n]

n = int(input())
cnt_recur = cnt_dp= 0
dp = [0]*(n+1)
dp[1]=1
dp[2]=1
fibo_dp(n)
fibo_recur(n)
print(cnt_recur+1, cnt_dp)