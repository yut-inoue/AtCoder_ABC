n=int(input())
#a,b=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

def prime_factorize(n):
    n_origin=n+0
    primelist=[]
    a=2
    while a*a<=n_origin:
        if n%a!=0:
            a+=1
            continue
        ex=0
        while n%a==0:
            ex+=1
            n=n//a
        primelist.append([a,ex])
        a+=1
    if n!=1:
        primelist.append([n,1])
    return primelist

def countf(e):
    v=0
    count=0
    while True:
        if v+(count+1)>e:
            break
        count+=1
        v+=count
    return count

primel=prime_factorize(n)
ans=0

for l in primel:
    p,e=l
    ans+=countf(e)

print(ans)