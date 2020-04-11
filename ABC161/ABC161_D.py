k=int(input())
#a,b=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

from collections import deque

q=deque([1,2,3,4,5,6,7,8,9])
ansl=[]
s=1
while len(str(s))<=10:
    s=q.popleft()
    ansl.append(s)
    sl=list(str(s))
    last_digit=int(sl[-1])
    for digit in range(max(0,last_digit-1),min(last_digit+1,9)+1):
        newval=int(str(s)+str(digit))
        #ansl.append(int(str(s)+str(digit)))
        q.append(newval)
print(ansl[k-1])