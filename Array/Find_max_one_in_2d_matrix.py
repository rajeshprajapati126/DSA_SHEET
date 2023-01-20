# Row with max 1s

# Given a boolean 2D array of n x m dimensions where each row is sorted. 
# Find the 0-based index of the first row that has the maximum number of 1's.

# Input: 
# N = 4 , M = 4
# Arr[][] = {{0, 1, 1, 1},
#            {0, 0, 1, 1},
#            {1, 1, 1, 1},
#            {0, 0, 0, 0}}
# Output: 2
# Explanation: Row 2 contains 4 1's (0-based
# indexing)
def rowWithMax1s(arr, n, m):
    max=0
    sum=0
    res=0
    col=m-1
    for i in range(n):

        while col>=0:
            if arr[i][col]==0:
                break
            else:
                sum+=1
            col-=1
        if max<sum:
            res=i
            max=sum
    
    return res 
arr=[[0, 1, 1, 1],
[0, 0, 1, 1],
[1, 1, 1, 1],
[0, 0, 0, 0]]
n=3
m=3
print(rowWithMax1s(arr,n,m))

            