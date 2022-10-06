import sys
import re
string = sys.stdin.readline().strip()
pattern = re.compile("(<.+?>)|([^<>]+)")
string = re.split(pattern,string)
result = []
for i in string:
    if i=='' or i is None:
        continue
    elif i[0].startswith('<'):
        result.append(i)
    else:
        tmp =''
        for i in i.split():
            tmp +="".join(reversed(i))
            tmp+=" "
        result.append(tmp.strip())
for i in result:
    print(i,end='')
