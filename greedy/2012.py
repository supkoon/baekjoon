'''
문제
시험에 n명의 학생들이 참가
예상등수 적어서 냄

예상 등수를 바탕으로 등수 냄
이떄의 불만도는 abs(a-b)

불만도를 최소로 하기.


아이디어 

'''
import sys 
n = int(input())
rank = list()
for i in range(n):
    rank.append(int(sys.stdin.readline().rstrip()))
rank.sort()
result = 0
for i in range(1,n+1):
    result += abs(rank[i-1]-i)
print(result)