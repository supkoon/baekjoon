'''
문제
설탕배달
N킬로 배달
3킬로 봉지 5킬로 봉지
최대한 적은 봉지
정확하게 N킬로 배달 


'''
def solution(n):
    dp = [0] *(5000+1)
    dp[3] = 1
    dp[4] = -1
    dp[5] = 1
    for i in range(6,n+1):
        if dp[i-3]>0 and dp[i-5]>0:
            dp[i] = min(dp[i-3],dp[i-5])+1
        elif dp[i-5]>0:
            dp[i] = dp[i-5]+1
        elif dp[i-3]>0:
            dp[i] = dp[i-3]+1
        else:
            dp[i] = -1
    return dp[n]


n = int(input())
print(solution(n))
