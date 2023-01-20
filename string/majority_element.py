
arr=list(map(int,input().split(",")))

ele=0
cnt=0
for i in range(len(arr)):
    if cnt==0:
        ele=arr[i]
    if ele==arr[i]:
        cnt+=1
    else:
        cnt-=1
count=0
for i in range(len(arr)):
    if arr[i]==ele:
        count+=1
if count==(len(arr)//2):
    print(ele)
else:
    print(-1)

    