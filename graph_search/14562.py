from collections import deque
n = map(int,input().split())

def bfs(start,goal):
    queue = deque()
    cnt = 0
    queue.append([start,goal,cnt])
    while(queue):
        start,goal,cnt = queue.popleft()
        if start<goal:
            queue.append([start*2,goal+3,cnt+1])
            queue.append([start+1,goal,cnt+1])
        elif start==goal:
            print(cnt)
            break

