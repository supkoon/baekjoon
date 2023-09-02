'''
문제
N과 M
중복조합
내림차순이 아니어야함. (이상)


아이디어 
백트랙킹 + 이상으로.
'''
answer =0 
def dfs(start,cur,n,m):
    global answer
    #pruning
    if len(cur)==m:
        print(' '.join(map(str,cur)))
        return 
    #search dfs
    for num in range(start,n+1):
        cur.append(num)
        dfs(num,cur,n,m)
        cur.pop()

def solution(n,m):
    global answer

    dfs(1,[],n,m)

n,m = map(int,input().split())
solution(n,m)

