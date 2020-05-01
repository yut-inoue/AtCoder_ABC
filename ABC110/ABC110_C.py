#n=int(input())
#a,b=map(int,input().split())
sl=list(input())
tl=list(input())
#l=[list(map(int,input().split())) for i in range(n)]

sdic={}
tdic={}
flag=True
for i in range(len(sl)):
    s=sl[i]
    t=tl[i]
    if sdic.get(s,-1)==-1:
        sdic[s]=t
    else:
        if sdic[s]!=t:
            flag=False
            break
    if tdic.get(t,-1)==-1:
        tdic[t]=s
    else:
        if tdic[t]!=s:
            flag=False
            break
if flag:
    print('Yes')
else:
    print('No')

