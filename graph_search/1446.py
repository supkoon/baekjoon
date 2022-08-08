import sys
from collections import deque
n,d = map(int,sys.stdin.readline().split())
shortcuts=[list(map(int,input().split())) for _ in range(n)]
def bfs(end):
    queue = deque()
    queue.append([0,0])
    results=[]
    while(queue):
        cur , count = queue.popleft()
        for shortcut in [i for i in shortcuts if i[0]==cur]+[[cur,cur+1,1]]:
            if shortcut[1]==d:
                results.append(shortcut[2]+count)
            elif shortcut[1] < d:
                queue.append([shortcut[1],count+shortcut[2]])
    return min(results)
print(bfs(d))