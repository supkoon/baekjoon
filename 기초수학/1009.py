import sys
n = int(sys.stdin.readline())
for line in range(n):
    a,b = map(int,sys.stdin.readline().split())
    nums = list()
    for i in range(1,5):
        last = a**i%10
        if last ==0:
            last = 10
        if last not in nums:
            nums.append(last)
    sys.stdout.write(str(list(nums)[b%len(nums)-1])+"\n")
