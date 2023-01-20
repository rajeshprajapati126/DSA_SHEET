n=int(input())
for i in range(n):
    str1=""
    r=n
    for i in range(i*2+1):
        str1+="*"
    print(str1.center(2*(r)))
    r-=1