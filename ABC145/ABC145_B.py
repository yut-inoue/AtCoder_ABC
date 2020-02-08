n=int(input())
s=list(input())

if n%2==0:
    mid=int(n/2)
    prv=s[0:mid];lat=s[mid:n]
    if prv==lat:
        print("Yes")
    else:
        print("No")
else:
    print("No")
