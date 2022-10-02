n = int(input())
nums = map(int,input().split())
nums = sorted(nums)
m = int(input())

start = 0
end = nums[-1]

def check(x,thres):
    return min(thres,x)
def binary_search(target,nums,start,end):
    if start>end:
        return end
    mid = (start+end)//2
    total = sum(map(lambda x: min(mid,x),nums))
    if total<=target:
        return binary_search(target,nums,mid+1,end)
    elif total>target:
        return binary_search(target,nums,start,mid-1)
print(binary_search(m,nums,start,end))

