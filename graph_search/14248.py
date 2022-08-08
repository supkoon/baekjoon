from collections import deque
n = int(input())
n_jumps = list(map(int,input().split()))
n_jumps = [0] +n_jumps
start = int(input())
visited = [0] * (n + 1)


def bfs(start):
    global n_jumps
    global visited
    queue = deque()
    queue.append(start)
    visited[start]=True

    while(queue):
        expanded = queue.popleft()
        for child in [expanded-n_jumps[expanded],expanded+n_jumps[expanded]]:
            if (0<child<=n) and not visited[child] :
                queue.append(child)
                visited[child]=True
    return sum(visited)
print(bfs(start))


