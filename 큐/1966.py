from collections import deque
n = int(input())

for case in range(n):
    n,m = map(int,input().split())
    papers = list(map(int,input().split()))
    queue=deque()
    for i in papers:
        queue.append(i)
    while(queue):
        first = queue.popleft()
        

