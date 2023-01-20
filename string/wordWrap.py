from cmath import inf
from sre_constants import RANGE_UNI_IGNORE


n=int(input())
a=[]
for i in range(1,n+1):
    a[i]=int(input())
m=int(input())
space=[[0 for i in range(0,n+1)] for i in range(0,n+1)]
ls=[[0 for i in range(0,n+1)] for i in range(0,n+1)]
c=[0 for i in range(0,n+1)]
p=[0 for i in range(0,n+1)]
for i in range(1,n+1):
    space[i][i]=m-a[i]
    for j in range(i+1,n+1):
        space[i][j]=space[i][j-1]-a[j] -1

for i in range(1,n+1):
    for j in range(i,n+1):
        if space[i][j]<0:
            ls[i][j]=inf
        elif (j==n and space[i][j]>=0): 
            ls[i][j]=0
        else :
            ls[i][j]=space[i][j]*space[i][j]

c[0]=0
for i in range(1,n+1):
    c[i]=inf
    for j in  range(1,i+1):
        if (c[j-1]!=inf and ls[j][i]!=inf and c[j-1]+ls[j][i]<c[i]):
            c[i]=c[j-1]+ls[j][i]
            p[i]=j
    
    