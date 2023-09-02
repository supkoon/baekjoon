'''
문제
nCm

'''

cur = []
def dfs(n,m):
    if len(cur)==m:
        print(' '.join(map(str,cur)))
        return # return 안해주면 더돌아버림  
    
    for i in range(1,n+1):
        cur.append(i)
        dfs(n,m)
        cur.pop()

def solution(n,m):
    dfs(n,m)

n,m = map(int,input().split())
solution(n,m)