a,b=map(int,input().split())
s=list(input())
flag='No'
if s[a]=='-' and s.count('-')==1:
    flag='Yes'
print(flag)