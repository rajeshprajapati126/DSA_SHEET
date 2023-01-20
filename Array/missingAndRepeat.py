arr=list(map(int,input().split(",")))


def findTwoElement(arr):
    n=len(arr)
    ans=[]
    count=[0]*(n+1)
    for i in range(n):
        count[arr[i]]+=1
    
    for j in range(1, len(count)):
        if count[j]>1:
            repeat=j
        if count[j]==0:
            miss=j
    return repeat,miss
    # n=len(arr)
    # ans=[]
    # for i in range(n):
    #     if arr[abs(arr[i])-1]>0:
    #         arr[abs(arr[i])-1]=-arr[abs(arr[i])-1]
    #     else:
    #         ans.append(abs(arr[i]))
    # for i in range(n):
    #     if arr[i]>0:
    #         ans.append(i+1)
    # return ans

print(findTwoElement(arr))