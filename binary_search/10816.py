# import sys
# n = int(sys.stdin.readline())
# nums = list(map(int,sys.stdin.readline().split()))
# start=0
# end=n-1
# m = int(sys.stdin.readline())
# target = list(map(int,sys.stdin.readline().split()))
# results=[]
#
# nums = sorted(nums)
# def binary_search(target,nums,start,end):
#     if start>end:
#         return -1
#     mid = (start+end)//2
#     if nums[mid] < target:
#         return binary_search(target,nums,mid+1,end)
#     elif nums[mid] > target:
#         return binary_search(target,nums,start,mid-1)
#     else:
#         return mid
#
# for i in target:
#     idx = binary_search(i,nums,start,end)
#     if idx>=0:
#         cnt_plus=0
#         while(idx+cnt_plus<n):
#             if nums[idx+cnt_plus]==nums[idx]:
#                 cnt_plus+=1
#             else:
#                 break
#         cnt_minus=0
#         while (idx+cnt_minus>=0):
#             if nums[idx + cnt_minus] == nums[idx]:
#                 cnt_minus -= 1
#             else:
#                 break
#         results.append(cnt_plus+-1*cnt_minus-1)
#     else:
#         results.append(0)
#
# print(' '.join(map(str,results)))

import sys
n = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
target = list(map(int,sys.stdin.readline().split()))
results = {}
for i in nums:
    if i in results:
        results[i]+=1
    else:
        results[i]=1

print(' '.join(str(results[i]) if i in results else '0' for i in target))