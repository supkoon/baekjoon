n = int(input())
total = 0
for i in range(n):
    a = input()
    result = 0
    unique = set(list(a))
    for j in unique:
        if a.find(a.count(j)*j) !=-1:
           result +=1
    if result == len(unique):
        total+=1
print(total)