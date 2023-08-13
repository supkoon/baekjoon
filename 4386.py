'''
문제
별자리 만들기
n개의 별을 이어서 별자리를 하나 만들것.
조건 : 일직선으로 이음, 모든 별은 직/간접으로 이어져있음

별자리를 만드는 최소비용은?

아이디어
MST
크루스칼 : 정렬복잡도 만큼 소모(일반적 O(nlogn))


'''
import sys

n = int(input())
stars = []
INF = 1e10
edges = []
parents = [x for x in range(n)]


for i in range(n):
    x,y = map(float,sys.stdin.readline().split())
    stars.append([x,y])
 
def dist(s1,s2):
    x1,y1 = s1
    x2,y2 = s2
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

for i in range(n):
    for j in range(i+1,n):
        w = dist(stars[i],stars[j])
        edges.append((i,j,w))
edges.sort(key = lambda x : x[2])

def find_root(parents,x):
    if parents[x]!=x:
        parents[x] = find_root(parents,parents[x])
    return parents[x]

def union_parent(parents,a,b):
    a = find_root(parents,a)
    b = find_root(parents,b)
    if a<b:
        parents[b] = a
    else:
        parents[a] = b

results = 0
for s,e,w in edges:
    if find_root(parents,s)!=find_root(parents,e):
        union_parent(parents,s,e)
        results+=w

print(round(results,2))