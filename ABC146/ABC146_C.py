a,b,x=map(int,input().split())

left=0
right=10**9
temp_ans=0

if a*right+b*(len(str(right)))<=x:
    print(right)
else:
    while left<right:
        mid=int((left+right)/2)
        if a*mid+b*(len(str(mid)))<=x:
            temp_ans=mid
            left=mid+1
        else:
            right=mid
    print(temp_ans)