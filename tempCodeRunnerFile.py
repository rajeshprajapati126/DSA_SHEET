n=len(arr)
prefix=[0]*n
product=1
# sufix=[0]*n
prefix[0]=arr[0]
# sufix[-1]=arr[-1]
for i in range(1,n):
    if arr[i]==0:
        prefix[i]=prefix[i-1]*arr[i]
for i in range(n-1,-1,-1):
    if i==0:
        prefix[i]=product
    elif i==(n-1):
        prefix[i]=prefix[-2]
    else:
        prefix[i]=prefix[i-1]*product
    product*=arr[i]