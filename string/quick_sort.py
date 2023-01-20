# arr=list(map(int,input().split(",")))

# def partition(arr,low,high):
    
#     pi=low
    
#     pivot=arr[high-1]
    
#     for i in range(low,high):
        
#         if arr[i]<pivot:
#             arr[i],arr[pi]=arr[pi],arr[i]
#             pi+=1
#     arr[i],arr[pivot]=arr[pivot],arr[i]
#     return pi

# def quickSort(arr,low,high):
#     if low<high:
#         pi=partition(arr,low,high)
#         quickSort(arr,low,pi-1)
#         quickSort(arr,pi+1,high)
#     return arr
# n=len(arr)
# a=quickSort(arr,0,n)
# print(a)


arr=[1,2,3,4,5,6,7,8]
for i,j in enumerate(arr):
    print(i,j)