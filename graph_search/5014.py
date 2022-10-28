from collections import deque
f,s,g,u,d = map(int,input().split())
#f = 건물
#s = 현
#g = 목적
#u,d

def bfs():
    global f,s,g,u,d
    visited = [0 for _ in range(f+1)]
    visited[s]=1
    queue=deque()
    queue.append(s)
    while(queue):
        floor = queue.popleft()
        for i in [u,-1*d]:
            floor_next = floor+i
            if 1<=floor_next<=f and not visited[floor_next]:
                queue.append(floor_next)
                visited[floor_next]=visited[floor]+1

                if floor_next == g:
                    break
    return visited[g]
result = bfs()
if result:
    print(result-1)
else:
    print('use the stairs')

