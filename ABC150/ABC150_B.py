n=int(input())
s=input()
count=0
if n==3:
    if s=="ABC":
        count=1
else:
    s=list(s)
    for i in range(n-3+1):
        if s[i]=="A" and s[i+1]=="B" and s[i+2]=="C":
            count+=1
print(count)


