n=int(input())
#a,b=map(int,input().split())
al=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

def chk(A):
    if all([ai%2==0 for ai in A]):
        return True
    else:
        return False
count=0
while chk(al):
    count+=1
    for i in range(n):
        al[i]=al[i]//2
print(count)