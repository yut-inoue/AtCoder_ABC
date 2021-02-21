#n = int(input())
#a, b = map(int,input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
ans='Yes'
s=list(input())
a=list('abcdefghijklmnopqrstuvwxyz')
for i in range(len(s)):
    if (i+1)%2!=0 :
        if not s[i] in a:
            ans='No'
            break
    else:
        if s[i] in a:
            ans='No'
            break

print(ans)