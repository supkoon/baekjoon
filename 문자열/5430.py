import sys
from collections import deque
n_case = int(sys.stdin.readline())
for i in range(n_case):
    func = list(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline())
    nums = sys.stdin.readline().rstrip()
    queue = deque()
    if n :
        for i in nums[1:-1].split(","):
            queue.append(i)
    flag=True
    cnt_R=0
    for j in func:
        if j =='R':#R이 연속일때 %2 만큼만.
            cnt_R+=1
        elif j=='D':
            if not queue:
                flag = False
                break
            if cnt_R%2:
                queue.pop()
            else:
                queue.popleft()
    if cnt_R%2:
        queue.reverse()
    if flag:
        print('['+','.join(queue)+']')
    else:
        print('error')