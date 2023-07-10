'''
문제
지민이가 모든 파티에 참가하여 이야기함.
N명, M개 파티
p 진실을 아는 사람 수, p_know 번호  



아이디어
각 사람이 어디에 속하는지 리스트 만든다. --> graph
각 파티에 누가있는지 리스트로 만든다 --> graph?
시작점(사실을 아는사람)을 기준으로 파티를 돌면서 거짓을 아는 탐색한다.
만약 방문하지 않은 파티라면 체크한다.

복잡도
O(n^3)?

변수
n,m 사람,파티수
p 사실아는사람 수
p_know 사실아는사람들 
parties 파티들 
graph 사람별로 어떤 파티에 가는지
visited_party : 거짓의 파티 방문여부(1이 방문안한것)

'''

n,m = map(int,input().split())
p = list(map(int,input().split()))
p, p_know = p[0],p[1:]


graph = [[] for _ in range(n+1)]

parties = []
for i in range(m):
    line = list(map(int,input().split()))
    # n_people = line[0] 
    people = line[1:]
    for j in people:
        graph[j].append(i)
    parties.append(people)

from collections import deque

visited_party = [1]*m

def bfs(person):
    global visited_party
    visited = [0]*(n+1) #이미 방문한 사람. 
    queue = deque()
    queue.append(person)
    visited[person] = 1 
    while(queue):
        expanded = queue.popleft()
        for child_party in graph[expanded]: #0,4
            for person_party in parties[child_party]:
                if not visited[person_party]:
                    queue.append(person_party)
                    visited[person_party] = 1

                if visited_party[child_party]:
                    visited_party[child_party] = 0


for person in p_know:
    bfs(person)

print(sum(visited_party))