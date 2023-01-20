Queries=[[2,4],[1,5]]

Queries.sort(key=lambda x:x[1])


arr=[1, 1, 2, 1, 3]
currL,currR,currCount=0,0,0

for i in range(len(Queries)):
    L,R=Queries[i]
    
    while currL<(L-1):
        if currL==1:
            currCount-=arr[currL]
        currL+=1
    while currL>(L-1):
        if currL==1:
            currCount+=arr[currL-1]
        currL-=1
    while currR<=(R-1):
        if currR==1: 
            currCount+=arr[currR]
        currR+=1
    while currR>R:
        if currR==1:
            currCount-=arr[currR-1]
        currR-=1
    
    print("Sum of",Queries[i],"is",currCount+1)



# for i in range(len(Queries)):
#     L,R=Queries[i]
    
#     while currL<L:
#         currSum-=arr[currL]
#         currL+=1
#     while currL>L:
#         currSum+=arr[currL-1]
#         currL-=1
#     while currR<=R:
#         currSum+=arr[currR]
#         currR+=1
#     while currR>R+1:
#         currSum-=arr[currR-1]
#         currR-=1
    
#     print("Sum of",Queries[i],"is",currSum)
    