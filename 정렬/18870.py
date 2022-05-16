import sys
n = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
nums_sorted = sorted(list(set(nums)))
nums_dict = dict()
for index,i in enumerate(nums_sorted):
    nums_dict.update({i:index})
for i in nums:
    sys.stdout.write(str(nums_dict[i])+" ")




