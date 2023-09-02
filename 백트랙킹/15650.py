'''
문제
nCm
오름차순만 인정

아이디어
백트랙킹 
+ 오름차순 반영 

child에서 i부터로 하면될듯? 
'''


def dfs(cur,n,m):
    
    if len(cur)==m:
        print(' '.join(list(map(str,cur)))) 
        return 
    
    if not cur:
        start = 1
    else:
        start = cur[-1] + 1
        
    for i in range(start,n+1):
        cur.append(i)
        dfs(cur,n,m)
        cur.pop()

def solution(n,m):
    dfs([],n,m)

n,m = map(int,input().split())
solution(n,m)

    