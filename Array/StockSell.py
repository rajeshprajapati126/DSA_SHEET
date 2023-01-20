n=int(input("Enter The Size"))
prc=list(map(int,input().split(",")))

def bestTimeToSell(arr,n):
    # aux=[0]*n
    # aux[-1]=arr[-1]
    # j=n-2
    # while j>=0:
    #     aux[j]=max(aux[j+1],arr[j])
    #     j-=1
    # i=0
    # max_=0
    # while i<n:
    #     max_c=aux[i]-arr[i]
    #     max_=max(max_,max_c)
    #     i+=1
    # return max_
    minsofar=arr[0]
    maxProfit=0
    for i in range(n):
        minsofar=min(arr[i],minsofar)
        profit=arr[i]-minsofar
        maxProfit=max(maxProfit,profit)
    return maxProfit
print(bestTimeToSell(prc,n))
        