tl=[int(input()) for i in range(5)]

import itertools

ansl=[]

for tup in itertools.permutations(tl):
    t=list(tup)
    c=0
    for i in range(4):
        c+=t[i]
        if c%10!=0:
            c=(c//10 +1)*10
    ansl.append(c+t[-1])

print(min(ansl))