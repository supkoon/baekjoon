'''
문제
N-queen

아이디어
row 별로 퀸의 col index를 저장
맨 처음 row부터 아래 row까지 도착할 경우 answer + 1

return 조건 : 맨 아래 row까지 도착한 경우(n)
안되는 조건 : 
col[i] == child (이미 해당 col에 있는경우) 불가능
abs(col[i]-y) == (x-i) x,y와 i,col[i]의 각각 거리가 같으면 대각에 있는거임 

'''

answer = 0


def dfs(x,n,cols): #x:몇개놨는지(몇 row인지)
    global answer 
    if x==n:
        answer+=1
        return 
    
   
    for col in range(n): #각각 col 가능한지 
        flag = 0 
        cols[x]=col
        for before_row in range(x): #row  x 이전까지 있었는지 확인 

            if cols[before_row]==col:
                flag=1
                break
            if abs(cols[before_row]-col)==x-before_row:
                flag=1
                break 

        if not flag:
            dfs(x+1,n,cols)
        

def solution(n):
    global answer
    cols= [-1]*n
    dfs(0,n,cols)
    return answer

n = int(input())
print(solution(n))