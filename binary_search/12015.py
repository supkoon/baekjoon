#복습하기.

import sys
n = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
dp=[0]
for i in range(n):
    #dp를 탐색
    start=0
    end = len(dp)-1
    while(start<=end):
        #nums[i] --> target
        mid = (start+end)//2
        if dp[mid]<nums[i]:
            start = mid+1
        else:
            end = mid-1
    if start>=len(dp):
        dp.append(nums[i])
    else:
        dp[start]=nums[i]
print(len(dp)-1)