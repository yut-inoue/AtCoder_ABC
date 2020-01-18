n=int(input())
pl=list(map(int,input().split()))
ql=list(map(int,input().split()))

import itertools
seq=[i for i in range(1,n+1)]
#print(list(itertools.permutations(seq)))
li=list(itertools.permutations(seq))
p=tuple(pl)
q=tuple(ql)

a=li.index(p)+1
b=li.index(q)+1

print(abs(a-b))