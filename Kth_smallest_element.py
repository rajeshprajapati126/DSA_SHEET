arr=[[1,3],[2,4],[6,8],[9,10]]
arr.sort()
print(arr)
def overlappedInterval( Intervals):
            #Code here
        Intervals.sort()
        mergeIntervals=[]
        tempInterval=Intervals[0]
        for ele in Intervals:
            if ele[0]<=tempInterval[1]:
                tempInterval[1]=max(ele[1],tempInterval[1])
            else:
                mergeIntervals.append(tempInterval)
                tempInterval=ele
        mergeIntervals.append(tempInterval)
        return mergeIntervals
print(overlappedInterval(arr))