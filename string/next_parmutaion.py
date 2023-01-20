from __future__ import barry_as_FLUFL


arr=list(map(int,input().split(',')))

n=len(arr)

ind1=-1
ind2=-1
i=n-2
while i>=0:
    if arr[i]<arr[i+1]:
        break
    i-=1
ind1=i

j=n-1
while j>=0:
    if arr[ind1]<arr[i]:
        break
    j-=1
ind2=j

#swap arr[ind1] to arr[ind2]

arr[ind1],arr[ind2]=arr[ind2],arr[ind1]
arr1=sorted(arr[ind1+1:n])

i=0
while i<(len(arr1)):
    indx=ind1+i+1
    arr[indx]=arr1[i]
    i+=1
print(arr)