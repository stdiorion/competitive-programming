from decimal import*;l=Decimal;_=l.__floor__
x,y,r=map(l,input().split())
print(sum(_(d:=x+(r*r-(y-h)**2).sqrt())+_(d-x-x)+1for h in range(-_(r-y),_(y+r+1))))