import sys
k,n = map(int,sys.stdin.readline().split())
nums = []
for i in range(k):
    nums.append(int(sys.stdin.readline()))
start = 1
end = max(nums)

def binary_search(target,nums,start,end):
    if start>end:
        return end
    mid = (start+end)//2
    cnt = sum(map(lambda x:x//mid,nums))

    if cnt >= target:
        return binary_search(target,nums,mid+1,end)
    else:
        return binary_search(target,nums,start,mid-1)
thres = binary_search(n,nums,start,end)
print(thres)



