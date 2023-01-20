from math import prod


arr=list(map(int,input("Enter Numbers:").split(",")))

n=len(arr)
prefix=[0]*n
product=1
# sufix=[0]*n
prefix[0]=arr[0]
# sufix[-1]=arr[-1]
for i in range(1,n):
    prefix[i]=prefix[i-1]*arr[i]
for i in range(n-1,-1,-1):
    if i==0:
        prefix[i]=product
    elif i==(n-1):
        prefix[i]=prefix[-2]
    else:
        prefix[i]=prefix[i-1]*product
    product*=arr[i]
print(prefix)








# n=len(arr)
# prefix=[0]*n
# sufix=[0]*n
# prefix[0]=arr[0]
# sufix[-1]=arr[-1]
# for i in range(1,n):
#     prefix[i]=prefix[i-1]*arr[i]
# for i in range(n-2,-1,-1):
#     sufix[i]=sufix[i+1]*arr[i]

# arr[0]=sufix[1]
# arr[-1]=prefix[-2]
# for j in range(1,n-1):
#     arr[j]=prefix[j-1]*sufix[j+1]
# print(arr,prefix,sufix)





# n=len(arr)
# product=1
# flag=0
# for i in range(n):
#     if arr[i]!=0:
#         product*=arr[i]
# for i in range(n):
#     if arr[i]==0:
#         ind=i
#         arr[i]=product
#         flag=1
#         break
#     arr[i]=product//arr[i]
# if flag==1:
#     for i in range(n):
#         if i != ind:
#             arr[i]=0
    
# print(arr)











# mul=1
# n=len(arr)
# res=[0]*n


# for i in range(n):
#     mul=1
#     for j in range(n):
        
#         if i==j:
#             continue
#         else:
#             mul=mul*arr[j]
# #     res[i]=mul
# print(res)