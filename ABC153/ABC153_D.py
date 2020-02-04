h=int(input())
count=1
ans=1
v=h
import math
while True:
    temp=math.floor(v/2)
    if temp==0:
        #count=count*2
        #ans+=1
        #ans+=count
        break
    v=temp
    ans+=1
    
print(int((1-2**(ans))/(1-2)))


