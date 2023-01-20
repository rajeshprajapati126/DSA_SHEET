str1=input()
str2=input()

dict1={}
dict2={}

for i in range(len(str2)):
    dict1[str2[i]]=1+dict1.get(str2[i],0)

mc=0
dmc=len(str2)
i=-1
j=-1
ans=""
while True:
    flag1=0
    flag2=0
    while i<len(str1)-1 and mc<dmc:
        i+=1
        dict2[str1[i]]=1+dict2.get(str1[i],0)
        if dict2.get(str1[i],0)<=dict1.get(str1[i],0):
            mc+=1
        flag=1
    while j<i and mc==dmc:
        psp=str1[j+1:i+1]
        if len(ans)==0 or len(ans)>len(psp):
            ans=psp
        j+=1
        if dict2.get(str1[j],0)==1:
            dict2.pop(str1[j])
        else:
            dict2[str1[j]]-=1
        if dict2.get(str1[j],0)<dict1.get(str1[j],0):
            mc-=1
        flag=1
    if flag1==0 and flag2==0:
        break
if len(ans)==0:
    print("-1")
else:
    print(ans)
            