n=int(input())
al=list(map(int,input().split()))

import fractions

def gcdoflist(l):
    n=len(l)
    if n==1:
        return l[0]
    else:
        ans=l[0]
        for i in range(1,n):
            ans=fractions.gcd(ans,l[i])
        return ans
m_list=[]
#端点の場合
#右端
m_list.append(gcdoflist(al[0:n-1]))

#左端
m_list.append(gcdoflist(al[1:n]))
ans=max(m_list)
for i in range(1,n-1):
    left=al[0:i]
    right=al[i+1:n]
    temp=fractions.gcd(gcdoflist(left),gcdoflist(right))
    if temp>ans:
        ans=temp
print(ans)

