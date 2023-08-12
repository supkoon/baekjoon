'''
문제
도시 분할 계획

마을 n개의 집 m개의 길, 양방향
길은 유지비 존재

마을을 두개로 분리
마을 사이의 길은 끊어도됨
마을 안에서도 임의의 두집 사이에 경로가 하나만 있으면됨.

유지비를 최소로 하면서 마을 나누기.

아이디어
MST 같음.
같은 마을을 하나로 이으면 됨. 




복잡도
'''
import sys 
n,m = map(int,sys.stdin.readline().split())
edges = []
for i in range(m):
    s,e,w = map(int,sys.stdin.readline().split())
    edges.append([s,e,w])
edges.sort(key = lambda x: x[2])
parent = [x for x in range(n+1)]


def find_root(parent,x):
    if parent[x] != x:
        parent[x] = find_root(parent, parent[x])

    return parent[x]

def union_parent(a,b,parent):
    a = find_root(parent,a)
    b = find_root(parent,b)

    if a<b:
        parent[b] = a
    else :
        parent[a] = b

result = []
for s,e,w in edges:
    if find_root(parent,s) != find_root(parent,e): #사이클이 발생하지 않으면,
        union_parent(s,e,parent)
        result.append(w)
print(sum(result[:-1]))

    