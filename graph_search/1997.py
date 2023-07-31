'''
최소 스패닝 트리 공부

스패닝 트리
최소 엣지로 모든 노드를 연결하는 그래프
n개의 노드를 n-1개의 엣지로 연결 

ex) 통신사에서 가장 적은 수의 케이블을 사용하여 전화기를 연결하고 싶은 경우
-->n-1개를 사용 

최소 스패닝 트리(MST)
간선들의 가중치까지 최소화하여 만든 스패닝 트리 
- 간선의 가중치 합 최소
- n-1개의 간선만을 사용
- 사이클이 있으면 안됨. 

ex) 전선의 길이 최소, 도로의 길이 최소, 전화선 길이 최소, 파이프 길이 최소 ,. . . 

MST 구현
Kruskal mst 

greedy.
각 단계에서 사이클을 이루지 않는 최소 비용 간선을 선택 

1.간선듦을 가중치 오름차순으로 정렬
2.순서대로 최소신장트리에 포함시킬지 포함시키지 않을지 판단. 
(사이클 발생 유무로)
3.해당 간선을 MST 집합에 추가 

복잡도
O(eloge)
간선 정렬시 사용됨. 표준 라이브러리 정렬 복잡도 --> ElogE 
'''
import sys 
def find_parent(parent,x):
    #루트노드 찾을때까지 재귀호출
    if parent[x]!=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]


def union_parent(parent,a,b):
    #두 노드의 루트가 다를때, 부모를 하나로 합치기 위함. 
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b


v,e= map(int,sys.stdin.readline().split())
parent = [i for i in range(v+1)]
edges = [list(map(int,sys.stdin.readline().split())) for _ in range(e)]
edges.sort(key = lambda x : x[2])
result = 0

for edge in edges:
    s,e,w = edge
    if find_parent(parent,s) != find_parent(parent,e):
        union_parent(parent,s,e)
        result += w 

print(result)