#n=int(input())
n,x,y=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

#adjl=[[0 for i in range(n)] for j in range(n)]

dic={}

for i in range(n):
    for j in range(i,n):
        #if i>=j:
        #    continue
        dis=j-i
        maybe=abs(x-(i+1))+1+abs(y-(j+1))
        dis=min(dis,maybe)
        #adjl[i][j]=dis
        dic[dis]=dic.get(dis,0)+1
"""
for i in range(n):
    for j in range(i,n):
        #if i>=j:
        #    continue
        dis=adjl[i][j]
        dic[dis]=dic.get(dis,0)+1
"""
for k in range(1,n):
    print(dic.get(k,0))
    