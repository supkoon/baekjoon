n = int(input())
people = []
result = [1 for i in range(n)]
for case in range(n):
    weight, height = map(int,input().split())
    people.append([weight,height])

for i in range(len(people)):
    for  j in range(i+1,len(people)):
        if people[i][0] < people[j][0]:
            if people[i][1] < people[j][1]:
                result[i]+=1
        elif people[i][0] > people[j][0]:
            if people[i][1] > people[j][1]:
                result[j]+=1

for i in result:
    print(i,end=' ')