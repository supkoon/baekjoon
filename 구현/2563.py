'''
문제
100x100 도화지에 10x10 색종이 막 붙여서 
넓이 구하기
i,j --> 왼쪽아래 모서리의 x,y 좌표

도화지 밖으로는 안나감


아이디어
도화지가 크지 않으니, 2차원 배열 만들어서 색칠하기. 
쉬운 방법이 있는데 왜 고민했지... 


복잡도


'''
import sys 

n = int(input())
paper = [[0]*100 for _ in range(100)]
cnt = 0
for i in range(n):
    x,y = map(int,sys.stdin.readline().split())
    #x : 열 y : 행
    
    for row in range(y,y+10):
        for col in range(x,x+10):
            if not paper[row][col]:
                paper[row][col] = 1
                cnt+=1
print(cnt)
