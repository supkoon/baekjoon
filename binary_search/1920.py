import sys
n = int(sys.stdin.readline())
list_1 = sorted(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
list_2 = map(int,sys.stdin.readline().split())

def binary(l,nums,start,end):
    if start>end:
        return 0
    mid = (start+end)//2
    if l==nums[mid]:
        return 1
    elif l<nums[mid]:
        return binary(l,nums,start,mid-1)
    else:
        return binary(l,nums,mid+1,end)


for l in list_2:
    start=0
    end = n-1
    print(binary(l,list_1,start,end))


