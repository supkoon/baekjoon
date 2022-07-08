import sys
n = int(sys.stdin.readline())
jobs = []
for job in range(n):
    t_i,s_i = map(int,sys.stdin.readline().split())
    jobs.append([t_i,s_i])
jobs.sort(key =lambda x: x[1])
t=0 # 시간 누적합 위한 변수 # 시작시간
while True:
    total_time = t
    for t_i,s_i in jobs:
        if total_time+t_i<=s_i:
            total_time+=t_i
        else :
            print(t-1)
            exit()
    t+=1
#
# from sys import stdin
#
# input = stdin.readline
#
#
# def solve():
#     N = int(input())
#     arr = [tuple(map(int, input().split())) for _ in range(N)]
#     arr.sort(key=lambda x: x[1])
#     ans = 10 ** 10
#
#     t = 0
#     for i in range(N):
#         t += arr[i][0]
#         ans = min(ans, arr[i][1] - t)
#
#     print(ans if ans >= 0 else -1)
#     return
