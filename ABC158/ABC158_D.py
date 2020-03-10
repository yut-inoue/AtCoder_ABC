#n=int(input())
#a,b=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

sl=list(input())
q=int(input())
l=[list(map(str,input().split())) for i in range(q)]

#print(l)

count=0
isR=False
from collections import deque
sl=deque(sl)
for i in range(q):
    order=l[i]
    if order[0]=="1":
        count+=1
        #反転
    if count%2==0:
        isR=False
    else:
        isR=True
    if order[0]!="1":
        f=order[1]
        c=order[2]
        temp_f=f
        if isR:
            if temp_f=="1":
                temp_f="2"
            else:
                temp_f="1"
        if temp_f=="1":
            #tempq=deque(sl)
            sl.appendleft(c)
            #tempq.appendleft(c)
            #sl=list(tempq)
        else:
            sl.append(c)
sl=list(sl)
ln=len(sl)
ansl=[]
if isR:
    for i in range(ln-1,-1,-1):
        ansl.append(sl[i])
else:
    ansl=sl
ans=''.join(ansl)
print(ans)
