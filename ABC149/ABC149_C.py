x=int(input())
import math
def isprime(n):
    flag=True
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            flag=False
            break
    return flag
while True:
    if isprime(x):
        break
    x+=1
print(x)