str1=input()
res=[]
for i in str1:
    if len(res)==0:
        res.append(i)
    else:
        if res[-1]!=i:
            res.append(i)
print(res)