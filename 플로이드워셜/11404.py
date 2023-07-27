'''
플로이드 워셜
- 모든 정점에서 다른 모든 정점까지의 최소경로를 구하는 방법.
다익스트라와 다른점은 한 정점에서 다른 모든 정점이 아닌, 모든 정점에서 모든 정점이라는 것. 

두 정점 s,e 사이의 경유지m을 갔을때와 안갔을 때를 비교함.

모든 정점사이의 최단거리를 구해야함 --> 2차원 배열 필요

거처가는 정점을 기준으로 최단거리를 계산

-->3중 for문 사용 
노드의 수 N개. 현재 노드를 거쳐가는 모든 경로 --> 2중for문 --> 3중for문 


복잡도
3중for문 --> O(N^3)

구현할때, 중점m을 가장 윗 레벨의 for문으로 돌려야함. 

'''
import sys 


n = int(input())
m = int(input()) 

INF = 1e7
distance = [[INF] * (n+1) for _ in range(n+1)]

for i in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    distance[a][b] = min(c, distance[a][b])

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            distance[i][j] = 0

def floyd():
    for m in range(1,n+1):
        for s in range(1,n+1):
            for e in range(1,n+1):
                distance[s][e] = min(distance[s][e], distance[s][m] + distance[m][e])
floyd()


for i in range(1,n+1):
    for j in range(1,n+1):
        if distance[i][j]==INF:
            print(0, end =' ')
        else: print(distance[i][j],end=' ')
    print()

