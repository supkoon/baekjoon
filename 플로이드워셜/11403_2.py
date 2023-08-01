'''
플루이드 워셜 복습

플루이드 워셜은 모든 정점에서 다른 정점까지의 최단거리를 구하는 알고리즘. 
이중리스트가 필요합니다. 아닌가요? 

'''

import sys 
graph = [] 

n = int(input())
INF = 1e7

for i in range(n):
    line = list(map(int,input().split()))
    for j in range(n):
        if line[j]==0:
            line[j] = INF
    graph.append(line)

for m in range(n):
    for s in range(n):
        for e in range(n):
            if graph[s][e] > graph[s][m] + graph[m][e]:
                graph[s][e]  = graph[s][m] + graph[m][e]


for i in range(n):
    for j in range(n):
        if graph[i][j]!=INF:
            print(1,end=' ')
        else:
            print(0,end=' ')
    print()