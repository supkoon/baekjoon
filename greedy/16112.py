n , k = map(int,input().split())
quests = list(map(int,input().split()))
quests = sorted(quests)
total=0
for i in range(n):
    if i>=k:
        total+=k*quests[i]
    else:
        total+=i*quests[i]
print(total)
