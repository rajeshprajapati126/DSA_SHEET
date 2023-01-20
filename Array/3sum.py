nums=list(map(int,input("Enter Numbers:").split(",")))
res=set()
n=len(nums)
for i in range(n-2):
    if i==0 or (i>0 and nums[i]!=nums[i-1]):
        l=i+1
        h=n-1
        sum=0-nums[i]
        while (l<h):
            if (nums[l]+nums[h]==sum):
                res.add(nums[i],nums[l],nums[h])
                while (l<h and nums[l]==nums[l+1]):
                    l+=1
                while (l<h and nums[h]==nums[h-1]):
                    h-=1
                l+=1
                h-=1
            elif (nums[l]+nums[h]<sum):
                l+=1
            else:
                h-=1
print(res)