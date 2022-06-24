n = int(input())
cnt=0
people=[]
for i in range(n):
    people.append(int(input()))
dasom = people[0]
other = people[1:]
if n==1:
    print(cnt)
else :
    other.sort(reverse=True)
    while(dasom <= other[0]):
        other[0]-=1
        dasom+=1
        cnt+=1
        other.sort(reverse=True)
    print(cnt)
