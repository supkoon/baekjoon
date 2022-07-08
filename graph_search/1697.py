import sys
from collections import deque
start,end = map(int,sys.stdin.readline().split())

def bfs():
    queue=deque()
    queue.append(start)
    while(queue):
        expanded = queue.popleft()
        if expanded == end:
            print(visited[expanded])
            break
        for dx in [expanded+1,expanded-1,expanded*2]:
            if 0<=dx<=max and not visited[dx] :
                visited[dx]=visited[expanded]+1
                queue.append(dx)
max=10**5
visited = [0] * (max+ 1)
bfs()