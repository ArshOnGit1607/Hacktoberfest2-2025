x1,y1,x2,y2,r=map(int,input().split())
distance_x=int(abs(((x2-x1)**2)+((y2-y1)**2))**(1/2))
if distance_x<=2*r:
    print("YES")
else:
    print("NO")
