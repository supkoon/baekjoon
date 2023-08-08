'''
문제
게임의 n개 레벨
점수의 합으로 순위

레벨은 난이도순
하지만 점수는 아님. 따라서 특정 레벨 점수를 조정 --> 점수도 증가하도록

점수가 주어졌을 떄 몇번 감소시키면ㄷ ㅚ는지 



아이디어
위에서부터 내려가면서 1차이로 만들기.

복잡도

'''

import sys
n = int(input())

scores = []
for i in range(n):
    scores.append(int(sys.stdin.readline().rstrip()))

cnt=0
for i in range(n-1,0,-1):
    if scores[i]<=scores[i-1]:
        cnt+= scores[i-1]-scores[i]+1
        scores[i-1] = scores[i]-1
        
        
print(cnt)
