n=int(input("Enter Size Of Array:"))
nums=[int(input()) for _ in range(n)]
def maxSubArray(nums):
    max_c=0
    max_=-99999999
    n=len(nums)
    for i in range(n):
        max_c+=nums[i]
        max_=max(max_c,max_)
        if max_c<0:
            max_c=0
    return max_

print(maxSubArray(nums))