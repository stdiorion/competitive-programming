i=input
n=h=int(i())
l=m=_=0
while 1:l,h,_=[(m,h,q:=(s:=i("%d\n"%m)[0])=="V"and exit()or s=="M"),(l,m,q)][_^q==m-l&0];m=(h+l)//2