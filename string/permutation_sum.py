a=list(map(int,input().split(",")))
b=list(map(int,input().split(",")))
a.sort(reverse=True)
b.sort()
k=int(input())
flag=0
for i in range(len(a)):
    if a[i]+b[i]<k:
        flag=1
        print("True")       
if flag==0:
    print(True)