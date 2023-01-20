from re import L


arr=list(map(int,input("Enter Array:").split(',')))
sum=int(input("Enter Value of Sum:"))
n=len(arr)


def findSumPair_n_log_n(arr,sum): #IN O(nlogn)
    arr.sort()
    l=0
    n=len(arr)
    r=n-1
    while l<r:
        if arr[l]+arr[r]==sum:
            return True
        elif arr[l]+arr[r]<sum:
            l+=1
        else:
            r-=1
    return False

def findSumPair_n(arr,sum): #in O(n)
    for i in range(n-1):
        if arr[i]>arr[i+1]:
           break

    l=(i+1)%n
    r=i
    while l!=r:
        if arr[l]+arr[r]==sum:
            return True
        elif arr[l]+arr[r]<sum:
            l=(l+1)%n
        else:
             r=(n+r-1)%n    
    return False

# ans=findSumPair(arr,sum)
# print(ans)