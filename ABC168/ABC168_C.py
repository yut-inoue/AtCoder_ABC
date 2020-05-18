a,b,h,m=map(int,input().split())

long_deg=30*h+30*(m/60)
min_deg=6*m

deg=abs(long_deg-min_deg)

import math

ans=a**2+b**2-2*a*b*math.cos(math.radians(deg))
ans=math.sqrt(ans)

print('{:.11f}'.format(ans))