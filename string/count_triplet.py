arr=list(map(int,input().split(",")))
n=len(arr)
ans=0
sumo=int(input())
arr.sort()
for i in range(n-2):
    j=i+1
    k=n-1
    while j<k:
        if arr[i]+arr[j]+arr[k]>=sumo:
            k-=1
        else:
            ans+=(k-j)
            j+=1
print(ans)