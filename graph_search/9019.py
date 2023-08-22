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

def make_str(x):
    x = str(x)
    x = (4-len(x))*'0' + x
    return x

def bfs(start,end):
    visited = [0]*10000
    visited[start]=1
    queue = deque()
    queue.append(start)
    while(queue):
        expanded = queue.popleft()
        for idx in range(4):
            if idx ==0:
                child = (expanded *2) %10000 
            
            elif idx ==1:
                pass 
            
            elif idx ==2:
                child = make_str(child)

            
            else:
                child = make_str(child)





for case in range(t):
    a,b = map(int,sys.stdin.readline().split())












