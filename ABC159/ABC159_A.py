#n=int(input())
n,m=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
import math
def combinations_count(n,k):#nCkを返す
    if k==0 or k==n:
        return 1
    elif n<k or k<0:
        return 0
    else:
        return math.factorial(n)//(math.factorial(n-k)*math.factorial(k))
print(combinations_count(n,2)+combinations_count(m,2))


