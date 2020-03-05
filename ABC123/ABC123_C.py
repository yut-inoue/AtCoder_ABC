#n=int(input())
#n,m=map(int,input().split())
#sl=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

n=int(input())
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())

mn=min(a,b,c,d,e)
import math
print(math.ceil(n/mn)+4)
