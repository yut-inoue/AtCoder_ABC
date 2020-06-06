#n=int(input())
a,b=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

l=[a+b,a-b,a*b]

print(max(l))

