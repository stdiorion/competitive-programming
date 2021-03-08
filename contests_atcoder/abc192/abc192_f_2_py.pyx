c="""#distutils:language=c++
#cython:language_level=3,boundscheck=False,wraparound=False,cdivision=True
from libcpp.vector cimport*
n,x,*A=map(int,open(0).read().split())
o=9**23
for 0<k<=n:
 d=vector[int](-~n*n,-9**23);d[0]=0
 for a in A:
  for k>=i>0:
   for-1<j<k:
    d[i*n+j]=max(d[i*n+j],d[~-i*n+(j-a)%k]+a)
 o=min(o,(x-d[k*n+x%k])//k)
print(o)"""
import sys,os
if sys.argv[-1]=="ONLINE_JUDGE":
 with open("a.pyx","w")as f:
  f.write(c)
 os.system("cythonize -i -3 -b a.pyx")
import a