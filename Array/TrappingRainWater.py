from turtle import right


arr=list(map(int,input("Enter Element:").split(",")))

n=len(arr)

# leftmax=0
# rightmax=0
# i=0
# l=0
# r=n-1
# res=0
# while l<r:
#     if arr[l]<=arr[r]:
#         if arr[i]>=leftmax:
#             leftmax=arr[i]
            
#         else:
#             res+=(leftmax-arr[i]) 
#         l+=1
#         i+=1
#     else:
#         if arr[r]>=rightmax:
#             rightmax=arr[r]
#         else:
#             res+=(rightmax-arr[r])
#         r-=1
# print(res)













# prefix=[0]*n
# prefix[0]=arr[0]
# sufix=[0]*n
# sufix[-1]=arr[-1]
# for i in range(1,n):
#     prefix[i]=max(prefix[i-1],arr[i])
# for i in range(n-2,-1,-1):
#     sufix[i]=max(sufix[i+1],arr[i])
# res=0
# for i in range(n):
#     min_=min(prefix[i],sufix[i])
#     res+=min_ - arr[i]
# print(res)