import sys
from collections import deque
n_case = int(sys.stdin.readline())
def manhattan(node_1,node_2):
    return abs(node_1[0]-node_2[0])+abs(node_1[1]-node_2[1])
def bfs(start,graph):
    queue= deque()
    queue.append(start)
    visited = [False for node in range(len(graph))]
    while(queue):
        expanded = queue.popleft()
        for child in graph[expanded]:
            if not visited[child]:
                queue.append(child)
                visited[child]=True
    return visited
#each case
for case in range(n_case):
    #편의점 수
    n = int(sys.stdin.readline())

    #node location dict
    nodes={node : None for node in range(n+2)}
    for node in range(n+2):
        x,y = map(int,sys.stdin.readline().split())
        nodes[node]=[x,y]
    # graph
    graph = [[] for node in range(n + 2)]

    for node in range(n+2):
        # 각 노드 기준으로 나머지 노드 중에 맨하탄 2000이하 child로 추가
        for other in range(n+2):
            if other!=node and manhattan(nodes[node],nodes[other])<=1000:
                graph[node].append(other)
    visited =bfs(0,graph)
    if visited[-1]:
        print("happy")
    else :
        print("sad")
