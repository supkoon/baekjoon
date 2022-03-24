#입력에서 가장 많은 알파벳 여러개일때는  ?
a =  list(input().upper())
only = list(set(a))
count_list = [a.count(i) for i in only]
count_max = max(count_list)
count = 0
for i in count_list:
    if i ==count_max:
        count+=1
if(count==1):
    for i in range(len(only)):
        if count_list[i]==count_max:
            print(only[i])
else:
    print("?")
