i=input;h=int(i())
Q=lambda q:(s:=i("%d\n"%q)[0])=="V"and exit()or"M"==s
l,m,_=0,h//2,Q(0)
while 1:l,h,_=[(m:=(h+l)//2,h,s:=Q(m)),(l,m,_)][_^s==m-l&0]