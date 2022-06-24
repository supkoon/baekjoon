string = list(map(int,list(input())))
cnt=0
for i in range(1,len(string)):
    if string[i]==string[i-1]:
        continue
    else:
        before = string[i-1]
        cnt +=1
        pointer = i
        while(string[pointer]!=before):
            string[pointer]=before
            pointer+=1
            if pointer > len(string)-1:
                break
print(cnt)
#앞에꺼랑 다르면 1씩 더할수도 있음.