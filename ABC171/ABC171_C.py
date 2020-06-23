n=int(input())
#x,n=map(int,input().split())
#pl=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

res=''
#res+=chr(ord("a")+n%26-1)
#n//=26
while n>0:
    n-=1
    res+=chr(ord("a")+n%26)
    n//=26
print(res[::-1])
