from collections import deque
n = int(input())

for case in range(n):
    n,m = map(int,input().split())
    papers = list(map(int,input().split()))
    queue=deque()
    flag= True
    for i in papers:
        queue.append(i)
    while(queue):
        first = queue.popleft()
        for i in queue:
            if first<i:
                queue.append(first)
                flag = False
                break
        if flag = pass
