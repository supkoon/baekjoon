n = int(input())
nums = list(map(int,input().split()))
nums=sorted(nums)
m =int(input())
targets = list(map(int,input().split()))

def binary_search(target,nums,start,end):
    if start>end:
        return 0
    mid = (start+end)//2
    if nums[mid]==target:
        return 1
    elif nums[mid]<target:
        return binary_search(target,nums,mid+1,end)
    else:
        return binary_search(target,nums,start,mid-1)

for i in targets:
    print(binary_search(i,nums,0,n-1),end=' ')
