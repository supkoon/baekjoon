import sys
n,c = map(int,sys.stdin.readline().split())
nums = []
for i in range(n):
    nums.append(int(sys.stdin.readline()))
nums = sorted(nums)

start = 1
end = nums[-1]-nums[0]
def binary_search(target, nums, start, end):
    if start>end:
        return end
    mid = (start+end)//2
    cur = nums[0]
    count=1

#몇개 되는지 체크. --> 이부분이 감 안왔음
    for i in range(1,n):
        if nums[i] - cur >= mid:
            cur = nums[i]
            count+=1
######
    if count >=target:
        return binary_search(target,nums,mid+1,end)
    else:
        return binary_search(target,nums,start,mid-1)
print(binary_search(c,nums,start,end))







