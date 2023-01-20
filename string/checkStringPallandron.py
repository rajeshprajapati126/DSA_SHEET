strg=input("Enter Valid String:")
n=len(strg)
strg=strg.lower()
str1=''
for i in range(n):
    if (ord(strg[i])>=65 and ord(strg[i])<=122) or (ord(strg[i])>=48 and ord(strg[i])<=57):
        str1+=strg[i]

n1=len(str1)
l=0
r=n1-1
while l<=r:
    if str1[l]!=str1[r]:
        print("False")
        break
    l+=1
    r-=1
