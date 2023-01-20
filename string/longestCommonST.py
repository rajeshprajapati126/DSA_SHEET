import math
from pickletools import string1, string4
import string


string1=list(map(str, input().split(",")))
n=len(string1)

match=string1[0]
for i in range(1,n):
    res=""
    for j in range(len(string1[i])):
        if len(match)>j and match[j]==string1[i][j]:
            res+=match[j]
            
    match=res
print(match)