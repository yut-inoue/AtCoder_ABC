n=int(input())
#a,b=map(int,input().split())
al=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

dic={}

for val in al:
    dic[val]=dic.get(val,0)+1

for i in range(1,n+1):
    print(dic.get(i,0))



