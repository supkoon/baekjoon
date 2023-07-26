'''
문제
1로 만들기 2 

1. 3으로 나누어 떨어지면 3으로 나눔
2. 2로 나누어 떨어지면 2로 나눔
3. 1을 뻄

+ 경로도 출력해야함.

아이디어
bfs 사용해보자(최단거리)
1부터 시작해서 찾기. 
이미 방문한 숫자면 멈추기.

복잡도
'''

# n = int(input())


# dp = [0]*(10**6+1)
# dp[1] = 0


# for i in range(2,n+1):
#     dp[i] = dp[i-1]+1
#     if i%3 ==0:
#         dp[i] = min(dp[i//3]+1,dp[i])
#     if i%2 ==0:
#         dp[i] = min(dp[i//2]+1,dp[i])

# print(dp[n])

from collections import deque

n = int(input())

visited = [0]*(10**6+1)
path = [0]*(10**6+1)

def bfs():
    global n 
    queue = deque()
    queue.append(1)
    visited[1] = 0

    while(queue):
        expanded = queue.popleft()
        for child in [1,2,3]:
            if child == 1:
                child = expanded + 1
            elif child == 2:
                child = expanded * 2
            elif child == 3:
                child = expanded * 3
            if child <=n and not visited[child]:
                    path[child] = expanded
                    visited[child] = visited[expanded]+1
                    if child == n:
                         return visited[child]
                    queue.append(child)
if n==1:
     print(0)
else:              
    print(bfs())

while(n>=1):
    print(n,end=' ')
    n = path[n]


