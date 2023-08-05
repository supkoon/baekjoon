'''

모든 간선이 양수일때, 한 정점에서 모든 다른 정점까지의 최단거리는 다익스트라 

음수 간선이 포함되었을때는?

--> 벨만포드, 하지만 속도는 다익스트라보다 느림
--> 벨만포드는 음의간선 순환을 찾을 수 있음. 


1. 출발노드 설정
2. 최단거리 테이블 초기화


3. 전체 간선확인 --> 각 간선을 거쳐 다른 노드로 가는 비용을 계산하여 최단거리테이블을 갱신
3을 n-1번 반복 
4. 한번 더 했을 때 테이블이 갱신되면 음의 간선 순환이 있는것. 

다익스트라 : 방문하지 않은 노드 중에서 최단거리 노드 선택(한 정점을 기준으로 가장 작은 노드만 우선순위큐에 추가하니깐)
벨만 포드 : 매번 모든 간선을 모두 확인 

'''


'''
문제
n개의도시(v)
m개의버스(e)
a,b,c = s,e,w
(w가 0 인경우, w가 음수인경우(순간이동) 이 있음;;)
1번도시를 기준으로 나머지 도시로 가는 가장 빠른시간

아이디어
하나의 정점으로부터 나머지 정점까지의 최단거리이며,
음의 간선이 존재할 수 있기 때문에,
다익스트라가 아닌 벨만포드 사용 

복잡도(O(VE)?)

'''
import sys 
INF = 1e9

def bf(start):
    distance[start] = 0 
#전체 n번의 라운드를 반복해야함 (n-1 + 1 )
    for i in range(n):
        # 매 반복마다 모든 간선을 확인 
        for j in range(m):
            s = graph[j][0]
            e = graph[j][1]
            w = graph[j][2]
            if distance[s] != INF and distance[e] > distance[s] + w:
                distance[e] = distance[s] + w 
                if i == n-1:
                    return True 
    return False 

graph = []
n,m = map(int,sys.stdin.readline().split())
distance = [INF for _ in range(n+1)]

for _ in range(m):
    line = list(map(int,sys.stdin.readline().split()))
    graph.append(line)

if bf(1):
    print('-1')
else:
    for i in range(2,n+1):
        if distance[i]==INF:
            print("-1")
        else:
            print(distance[i])