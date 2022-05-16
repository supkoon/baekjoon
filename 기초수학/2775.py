case = int(input())
result = []
for i in range(case):
    k = int(input())
    n = int(input())
    floors = []
    f_0 = [i for i in range(1,n+1)]
    floors.append(f_0)
    for j in range(1,k): # 층 쌓기
        floor = [1,]
        for l in range(1,n): # 방 쌓기 1 ~ n-1
            floor.append(sum(floors[j-1][:l+1])) #이전층의 l까지 합
        floors.append(floor)
    result.append(sum(floors[-1]))

for i in result:
    print(i)











