'''
문제
1부터 N까지 자연수 중 중복없이 M개를 고름
nCm?

'''
answer = [] 

def dfs(cur,m,visited):
    if len(cur) == m :
        print(' '.join(map(str,cur)))
        return
    
    for idx,is_visited in enumerate(visited[1:]):
        if not is_visited :
            cur.append(idx+1)
            visited[idx+1]=1
            dfs(cur,m,visited)
            cur.pop()
            visited[idx+1]=0


def solution(n,m):
    visited = [0]*(n+1) #1~N
    dfs([],m,visited)

n,m = map(int,input().split())
solution(n,m)
        
    