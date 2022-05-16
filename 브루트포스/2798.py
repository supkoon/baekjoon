import sys
n ,m  = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))

min = 0
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        for k in range(j+1,len(nums)):
            result = (sum([nums[i], nums[j], nums[k]]))
            if (m-result<m-min) & (m>=result):
                min = result

print(min)