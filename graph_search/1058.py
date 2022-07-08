import sys
from collections import deque
#graph init
n = int(sys.stdin.readline())
graph = [[] for node in range(n)]
for node in range(n):
    line = list(sys.stdin.readline())
    for idx,friend in enumerate(line):
        if friend=='Y':
            graph[node].append(idx)

#
def bfs(start,graph):
    visited = [0 for node in range(n)]
    friend_count = [0 for node in range(n)]
    queue = deque()
    queue.append(start)
    visited[start]=True
    while(queue):
        expanded = queue.popleft()
        if friend_count[expanded]<2:
            for child in graph[expanded]:
                if not visited[child]:
                    visited[child]=True
                    queue.append(child)
                    friend_count[child]=friend_count[expanded]+1
    return friend_count
# for lambda >0
def func(num):
    if num>0: return True
    else : return False
max=0
for idx in range(len(graph)):
    friend_count = bfs(idx, graph)
    result =sum(map(func,friend_count))
    if max< result:
        max = result
print(max)