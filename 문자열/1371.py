import collections
import re
import sys
a = sys.stdin.read()
chars = [x for x in list(re.sub('[^\w]','',a.lower()))]
counter = collections.Counter(chars)
#동률 고려해야함.
cnt_max = counter.most_common(1)[0][1]
for i in range(ord('a'),ord('z')+1):
    if counter[chr(i)]==cnt_max:
        print(chr(i),end='')