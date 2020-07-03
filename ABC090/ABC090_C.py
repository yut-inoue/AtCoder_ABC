n,m=map(int,input().split())

if n*m==1 :
    ans=1
elif n==1 or m==1 :
    ans=max(n,m)-2
else:
    ans=(m-2)*(n-2)
print(ans)