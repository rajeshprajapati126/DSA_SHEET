
m=int(input("Number Of Student:"))
n=int(input("Enter size of Array:"))
# packet=[int(input()) for _ in range(n)]
packet=list(map(int,input().split(',')))
def findMinDiff(packet,m,n):
    packet.sort()
    i=0
    j=i+m-1
    min_=999999999999
    while j<n:
       min_c=packet[j]-packet[i]
       
       min_=min(min_,min_c)
       i+=1
       j+=1
    return min_

c=findMinDiff(packet,m,n)
print(c)