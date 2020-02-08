n=int(input())
distance=[list(map(int,input().split())) for i in range(n)]

import itertools
import math
temp=[i for i in range(n)]
perm=list(itertools.permutations(temp))

sm=0
count=0
for route in perm:
    count+=1
    temp_dis=0
    route_list=list(route)
    for i in range(1,n):
        j=route_list[i]
        k=route_list[i-1]
        temp_dis+=math.sqrt((distance[j][0]-distance[k][0])**2+(distance[j][1]-distance[k][1])**2)
    sm+=temp_dis
ans=sm/count
print('{:.9f}'.format(ans))
