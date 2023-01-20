arr=[15, 4, 15]

def minMerge(arr):
    res=0
    i=0
    j=len(arr)-1
    while i<=j:
        if arr[i]==arr[j]:
            i+=1
            j-=1
        elif arr[i]<arr[j]:
            i+=1
            arr[i]=arr[i]+arr[i-1]
            res+=1
        else:
            j-=1
            arr[j]=arr[j]+arr[j+1]
            res+=1
    return res
print(minMerge(arr))

        