n,m =map(int,input().split())
nums = list(map(int,input().split()))
start = 0
end = max(nums)


def cut_lefted(num, thres):
    return max(0, num - thres)
def binary_search(target,nums,start,end):
    if start>end:
        return end
    mid = (start+end)//2
    left = sum(map(lambda x : cut_lefted(x,mid),nums))
    if target==left:
        return mid
    elif target>left:
        return binary_search(target,nums,start,mid-1)
    else:
        return binary_search(target,nums,mid+1,end)

print(binary_search(m,nums,start,end))

