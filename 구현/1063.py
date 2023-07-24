'''
문제
8x8 체스판 킹 하나
알파벳 : 열 A~H
숫자 : 행  1~8

킹의 무브
R : 한 칸 오른쪽으로
L : 한 칸 왼쪽으로
B : 한 칸 아래로
T : 한 칸 위로
RT : 오른쪽 위 대각선으로
LT : 왼쪽 위 대각선으로
RB : 오른쪽 아래 대각선으로
LB : 왼쪽 아래 대각선으로

킹이 돌을 드리블함.
만약 킹이나 돌이 나가게 된다면 그 무브는 생략함.

아이디어 
매번 움직임마다 진행해야할 조건, 통과해야할 조건 따지면서 가야할듯
ord와 chr을 이용해야겠음. 
시작점이 좌 하단임을 유의

복잡도
o(n)

변수 
x_king,y_king
x_stone,y_stone
move_map : 움직임 매핑해줄 딕셔너리

'''
move_map = {
    'R': (1,0),
    'L': (-1,0),
    'B': (0,-1),
    'T': (0,1),
    'RT' : (1,1),
    'LT' : (-1,1),
    'RB' : (1,-1),
    'LB' : (-1,-1)
}

xy_king,xy_stone,n = input().split()

x_king, y_king = list(xy_king)
x_king = ord(x_king)-64
y_king= int(y_king)

x_stone, y_stone = list(xy_stone)
x_stone = ord(x_stone)-64
y_stone= int(y_stone)

# print(x_king,y_king,x_stone,y_stone)

for _ in range(int(n)):
    move = input()
    dx, dy = move_map[move]
    nx_king, ny_king  = x_king+dx, y_king+dy
    nx_stone, ny_stone = x_stone,y_stone

    if not (1<=nx_king<=8 and 1<=ny_king<=8):
        continue

    # print(nx_king,ny_king)

    if x_stone==nx_king and y_stone==ny_king:
        nx_stone, ny_stone = x_stone + dx, y_stone + dy
      
    if not (1<=nx_stone<=8 and 1<=ny_stone<=8):
        continue
    
    # print(nx_king,ny_king,nx_stone,ny_stone)

    x_king, y_king = nx_king,ny_king
    x_stone, y_stone = nx_stone, ny_stone   
    
    
print(chr(x_king+64)+str(y_king))
print(chr(x_stone+64)+str(y_stone))
