from itertools import count


st=input("Enter valid string:")
R=int(input())
stc=[]
count=0
for i in st:
    if len(stc)==0:
        stc.append(i)
        count+=1
    elif stc[-1]==i and count==(R-1):
        while count:
            stc.pop()
            count-=1
    else:
        stc.append(i)
        count+=1
print(stc)
    