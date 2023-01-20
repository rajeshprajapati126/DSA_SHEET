def Pallindran(st):
    s=0
    e=0
    for i in range(len(st)):
        len1=expandSt(st,i,i+1)
        len2=expandSt(st,i,i)
        leng=max(len1,len2)
        if leng>(e-s):
            s=i-(leng-1)//2
            e=i+(leng)//2
    return st[s:e+1]

def expandSt(st,i,j):
    while i>=0 and j<len(st) and (st[i]==st[j]):
        i-=1
        j+=1
    return j-i-1

str1='bababaa'
print(Pallindran(str1))