s=list(input())
flag=True
for i in range(1,len(s)+1):
    v=s[i-1]
    if i%2==0:
        if v=="L" or v=="U" or v=="D":
            pass
        else:
            flag=False
            break
    else:
        if v=="R" or v=="U" or v=="D":
            pass
        else:
            flag=False
            break
if flag:
    print("Yes")
else:
    print("No")
