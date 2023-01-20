string=input("Enter String:")
k=int(input("K:"))
l=0
count={}
res=0
for r in range(len(string)):
    count[string[r]]=1+count.get(string[r],0)
    while (r-l+1)-max(count.values())>k:
        count[string[l]]-=1
        l+=1
    res=max(res,(r-l+1))
print(res)