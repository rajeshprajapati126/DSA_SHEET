arr=list(map(int,input().split(",")))
n=len(arr)
count_arr=[0 for i in range(max(arr)+1)] #store frequency of all element in arr
res=[0 for _ in range(len(arr))]
for i in range(len(arr)): #counting frequency
     count_arr[arr[i]]+=1
     
#modifiy count_arr for indexing link if 1 is repeated 4 times so it will fill the place of 0 to 3 and then other element is entered     
for i in range(1,len(count_arr)):
    count_arr[i]=count_arr[i-1]+count_arr[i]

#traverse original array and check count_arr by index and decrease one and then store element.

for i in range(n-1,-1,-1):
    count_arr[arr[i]]-=1
    res[count_arr[arr[i]]]=arr[i]
print(res)
