import sys
n  = int(input())

for i in range(n):
    m = int(input())
    cnt = 1
    people = [list(map(int,sys.stdin.readline().split())) for _ in range(m)]
    people = sorted(people)
    cutline = people[0][1]
    for j in range(1,m):
        if people[j][1]<cutline:
            cnt+=1
            cutline = people[j][1]
    print(cnt)
