import sys
n = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))

dp = [0]
for i in range(n):
    start = 0
    end = len(dp)-1
    while(start<=end):
       mid = (start+end)//2
       if dp[mid]<nums[i]:
           start = mid+1
       else :
           end = mid-1
#dp의 마지막보다 크면,
    if start>=len(dp):
        dp.append(nums[i])
#아니면 대치시킴.
    else:
        dp[start]=nums[i]
#대치시켜놓고, 더 있으면 찾는거고, 아니면 dp만 바뀌고 실제 string은 이전꺼로 길이는 유지되는거고..
print(len(dp)-1)




