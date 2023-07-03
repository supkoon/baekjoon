'''
문제
공기 정청기로 맵에 있는 미세먼지 청소.

각 칸에 있는 먼지는 사방으로 이동 ( 공기 청정기가 있거나 칸이 없으면 이동 x )
확산 양은 A//5
확산 후 남은 미세먼지 양은 A - A/5 x (방향 수)  

공기청정기는 위, 아래로 바람 뿜음
위는 반시계
아래는 시계로 돔, 
미세먼지는 바람의 방향대로 한칸씩 밀림. 공기청정기로 들어가면 없어짐. 

아이디어
한턴에 순서대로 먼지 날리기, 바람 날리기를 실행 
만약 바람이 먼지와 만났다면 상호작용 발생

복잡도


변수

'''
import sys

R,C,T = map(int,input().split())

graph = []

dust = []
machine = [] 

for i in range(R):
    line = list(map(int,sys.stdin.readline().split()))
    for j in range(C):
        if line[j] > 0 : 
            dust.append([i,j])
        elif line[j] < 0 :
            machine.append([i,j])  
    graph.append(line)

for i in range(R):
    print(wind_map[i])

def move_dust():
    pass
def move_wind():
    pass 
def move_wind_dust():
    pass  

flag = 1
while(flag):
    move_dust()

