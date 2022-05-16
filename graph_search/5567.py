from collections import deque
def bfs(start,graph):
  queue = deque()
  queue.append(start)
  visited = [0 for _ in range(len(graph))]
  cnt = [0 for _ in range(len(graph))]
  visited[start]=True
  while(queue):
    expanded = queue.popleft()
    for child in graph[expanded]:
      if not visited[child]:
        visited[child]=True
        cnt[child]=cnt[expanded]+1
        queue.append(child)
  return cnt

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for edge in range(m):
  friend_a, friend_b = map(int,input().split())
  graph[friend_a].append(friend_b)
  graph[friend_b].append(friend_a)

visited = bfs(1,graph)
cnt = 0
for i in visited:
  if 0<i<3:
    cnt+=1
print(cnt)