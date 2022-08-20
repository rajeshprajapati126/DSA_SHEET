n=int(input())
A=[int(input()) for _ in range(n)]
# for i in range(n):
#     a=int(input())
#     A.append(a)

def findSum(A,N): 
        #code here
    max_ele=A[0]
    min_ele=A[0]
    for i in range(1,N):
        if A[i]<min_ele:
            min_ele=A[i]
        elif A[i]>max_ele:
            max_ele=A[i]
    sum=max_ele+min_ele
    return sum

sum=findSum(A,n)
print(sum)