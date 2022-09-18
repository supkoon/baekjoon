n = int(input())




result = []

for line in range(n):
    ox = input()
    before = ox[0]
    combo = 1
    score = 0
    for i in range(len(ox)):
        right = (ox[i] =='O')
        score += combo * right
        if right : combo+=1
        else: combo=1
        before = ox[i]
    result.append(score)

for i in result:
    print(i)