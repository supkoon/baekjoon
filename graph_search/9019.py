'''
문제
dslr

계산기 명령어 d,s,l,r
계산기의 레지스터는 0~9999 저장가능
저장된 각 자리수를 d1,d2,d3,d4
d: n을 두배로, 10000이상일떈 10000으로 나눈 나머지
s: n-1, n이 0이면 9999로
l: 각 자리수를 왼쪽으로 이동 popleft pushright
r: 각 자리수를 오른쪽으로 이동 pop push0

a를 b로 바꾸는 최소한의 명령어

'''
import sys 
from collections import deque
t = int(input())

def bfs(start,end):
    visited = [0]*10000    
    visited[start]=1
    queue = deque()
    queue.append([start,''])

    while(queue):
        expanded,path = queue.popleft()
        for idx in range(4):
            #dslr
            if idx ==0:
                child = (expanded *2) %10000 
                
            elif idx ==1:
                child = expanded-1
                if child<0:
                    child = 9999
            
            elif idx ==2:
                child = expanded // 1000 + (expanded % 1000)*10

            else:
                child = expanded // 10 + expanded%10 * 1000
            if not visited[child] :
                visited[child] = idx
                queue.append([child , path+mapping[idx]])
                if child == end:
                    return path+mapping[idx]

mapping = ['D','S','L','R']
for case in range(t):
    a,b = map(int,sys.stdin.readline().split())
    print(bfs(a,b))
    