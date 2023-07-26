'''
다익스트라 복습
다익스트라 = dp + greedy 

그리디하게 방문하지 않은 노드중에서 가장 가까운 노드를 선택하여, 해당 위치에서 가장 가까운 노드를 반복적으로 선택함.

필요한것 . -- > 최단거리 테이블, 방문여부 테이블

heapq --> 우선순위 큐 구현위해 사용 --> 이진트리로 되어있어서 자동으로 가장 작은 값이 부모로 가게 정렬해줌. 자식간의 대소는 없음. 

문제
숨바꼭질. 
수빈이 N 동생 K에 있음.
수빈이 걷기, 순간이동 하기
걷기 --> 1초 x-1, x+1
순간이동 --> 0초 2*x

수빈이와 동생의 위치가 주어졌을 떄, 수빈이가 동생을 찾을 수 있는 가장 빠른시간

아이디어
bfs로 안되나?
0초와 1초가 있어서 간선의 길이가 있긴하네..
그래서 다익스트라 쓰는듯. 

복잡도

'''
import heapq
n,m = map(int,input().split())
INF = int(1e9)
distance = [INF]*200001 #뒤로도 갈수있으니깐 허용되는 범위에서 더 넓게 잡앗음.

def dijkstra(start):
    queue = []
    distance[start] = 0 # 자신까지 거리 0
    heapq.heappush(queue,[0,start]) #힙 구조에 시작노드의 키,노드 추가
    while(queue):
        dist,now = heapq.heappop(queue) #root 노드가 pop됨(key가 가장 작음.)
        if distance[now] < dist:
            continue #저장되어 있는 거리가 더 짧으면 이미 갱신되었음.
        
        for idx,child in enumerate([now+1,now-1,2*now]):
            if 0<=child<=200000:
                cost = dist 
                if idx!=2:
                    cost+=1
                if cost<distance[child]: #새로운 노드까지의 거리가 저장된 것보다 작으면 
                    distance[child] = cost
                    heapq.heappush(queue,[cost,child])
dijkstra(n)
print(distance[m])


