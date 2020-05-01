n=int(input())
#a,b=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
dic={}

for i in range(n):
    s=input()
    dic[s]=dic.get(s,0)+1

print(len(dic.keys()))
