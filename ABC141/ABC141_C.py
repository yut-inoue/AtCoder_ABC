n,k,q=map(int,input().split())

dic={}

for i in range(q):
    a=int(input())
    dic[a]=dic.get(a,0)+1

for i in range(1,n+1):
    win=dic.get(i,0)
    if k-(q-win)<=0:
        print("No")
    else:
        print("Yes")
