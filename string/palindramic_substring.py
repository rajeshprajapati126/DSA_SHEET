string=input()

table=[[0 for _ in range(len(string))] for _ in range(len(string))]
for i in range(len(string)):
    table[i][i]=1
for i in range(len(string)-1):
    if string[i]==string[i+1]:
        table[i][i+1]=1

k=3
while (k<=(len(string))):
    i=0
    while i<(len(string)-k+1):
        j=i+k-1
        if string[i]==string[j] and table[i+1][j-1]==1:
            table[i][j]=1
        i+=1
    k+=1
res=0
for i in range(len(string)):
    for j in range(len(string)):
        if table[i][j]==1:
            res+=1
print(res)
