import sys
n,m = map(int,sys.stdin.readline().split())
nums = [[0]+list(map(int,sys.stdin.readline().split())) for _ in range(n)]
nums = [[0]*(n+1)] + nums
x_max,y_max = 0,0
cases = []
for case in range(m):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    if x2>x_max:
        x_max = x2
    if y2>y_max:
        y_max = y2
    cases.append([x1,y1,x2,y2])

for i in range(1,x_max+1):
    for j in range(1,y_max+1):
            nums[i][j]=nums[i-1][j]+nums[i][j-1]-nums[i-1][j-1]+nums[i][j]
for x1,y1,x2,y2 in cases:
    result = nums[x2][y2]-nums[x1-1][y2]-nums[x2][y1-1]+nums[x1-1][y1-1]
    print(result)


