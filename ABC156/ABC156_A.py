#n=int(input())
n,r=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
if n>=10:
    print(r)
else:
    print(r+100*(10-n))