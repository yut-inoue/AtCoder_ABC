n=int(input())
#a,b=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
dic={}
dic['AC']=0
dic['WA']=0
dic['TLE']=0
dic['RE']=0
key=['AC','WA','TLE','RE']

for i in range(n):
    s=input()
    dic[s]=dic[s]+1

for k in key:
    print("{0} x {1}".format(k,dic[k]))