n=int(input())
al=list(map(int,input().split()))
flag=True
for i in range(n):
    v=al[i]
    if v%2==0:
        if (v%3==0) or (v%5==0):
            pass
        else:
            flag=False
            break
if flag:
    print("APPROVED")
else:
    print("DENIED")


