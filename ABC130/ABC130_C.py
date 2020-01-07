w,h,x,y=map(int,input().split())

area=w*h/2
count=0
if w/2==x and h/2==y:
    count=1
print('{:.10f} {}'.format(area,count))

