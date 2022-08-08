x = int(input())
line = input()
line = list(reversed(line))
w,m = 0,0
while(line):
    first =line.pop()
    if first =='W':
        if abs(w+1-m)<=x:
            w+=1
        elif line and abs(w+1-m)>x:
            second = line.pop()
            if second == 'M':
                if abs(m+1-w)<=x:
                    m+=1
                    line.append(first)
            else:
                break
        else:
            break
    else:
        if abs(m+1-w) <=x:
            m+=1
        elif line and abs(m+1-w) > x:
            second =line.pop()
            if second =='W':
                if abs(w+1-m)<=x:
                    w+=1
                    line.append(first)
            else:
                break
        else:
            break
print(w+m)





