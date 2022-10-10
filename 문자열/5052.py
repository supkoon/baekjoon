import sys

n = int(sys.stdin.readline().rstrip())
for case in range(n):
    n_case = int(sys.stdin.readline().rstrip())
    nums = [sys.stdin.readline().rstrip() for _ in range(n_case)]
    #문자열은 앞에서부터 ord로 정렬하기 때문에 그냥 sort로 가능.
    nums = sorted(nums)
    flag = False
    for i in range(n_case - 1):
        # print(nums[i+1],nums[i])
        if nums[i + 1].startswith(nums[i]):
            # print(nums[i],nums[i+1])
            flag = True
            break
    if flag:
        print('NO')
    else:
        print('YES')
