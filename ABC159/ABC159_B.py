#n=int(input())
#a,b=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

s=list(input())
n=len(s)
flag=True
stest=s[::-1]
if s!=stest:
    flag=False
stest=s[0:(n-1)//2]
if stest!=stest[::-1]:
    flag=False
stest=s[(n+3)//2-1:n]
if stest!=stest[::-1]:
    flag=False
if flag:
    print("Yes")
else:
    print("No")