'''
문제
가중치 없는 방향그래프 G가 주어졌을때,
모든 정점 i,j에 대해 i에서 j로 가는 길이가 양수인 경로가 있는지 없는지 구하기


아이디어
플로이드 워셜을 활용한 풀이



복잡도
플로이드 워셜 --> O(n^3) n^3은 2000까지 가능. 



'''
import sys 

n =int(input())
INF = 1e6
distance = [[INF] * (n) for _ in range(n)]

for i in range(n):
    line = list(map(int,sys.stdin.readline().split()))
    for j in range(n):
        if line[j]:
            distance[i][j]=1

for m in range(n):
    for s in range(n):
        for e in range(n):
            distance[s][e] = min(distance[s][m]+distance[m][e],distance[s][e])


for i in distance:
    for j in i:
        if j==INF:
            print(0,end=' ')
            
        else: print(min(j,1),end=' ')
    print()
    
