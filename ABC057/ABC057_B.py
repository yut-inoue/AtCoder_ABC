#n=int(input())
n,m=map(int,input().split())
#al=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(m)]

corl=[list(map(int,input().split())) for i in range(n)]
chkl=[list(map(int,input().split())) for i in range(m)]

for i in range(n):
    templ=[]
    a=corl[i][0]
    b=corl[i][1]
    for j in range(m):
        c=chkl[j][0]
        d=chkl[j][1]
        templ.append([j,abs(a-c)+abs(b-d)])
    templ.sort(key=lambda x:(x[1],x[0]))
    print(templ[0][0]+1)


