'''
문제
n,m 2차원 행렬에서
i,j 에서 x,y까지의 합을 구해주는 문제

아이디어

복잡도 

변수


'''


n,m = map(int,input().split())
matrix = []
for i in range(n):
    row = list(map(int,input().split()))
    matrix.append(row)
k = int(input())

for i in range(k):
    i,j,x,y = map(int,input().split())
    i,j,x,y = i-1,j-1,x-1,y-1

    result = 0

    for row in range(i,x+1):
        for col in range(j,y+1):
            result += matrix[row][col]

    print(result)