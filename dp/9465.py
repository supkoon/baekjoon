n = int(input())
for case in range(n):
    m = int(input())
    nums = [list(map(int,input().split())) for _ in range(2)]
    for j in range(1, m):
        if j==1:
            nums[0][j] = nums[1][j - 1] + nums[0][j]
            nums[1][j] = nums[0][j - 1]+ nums[1][j]
        else:
            a = max(nums[0][j - 2], nums[1][j - 2])
            nums[0][j] = max(nums[1][j - 1], a) + nums[0][j]
            nums[1][j] = max(nums[0][j - 1], a) + nums[1][j]
    print(max(nums[0][m-1],nums[1][m-1]))





