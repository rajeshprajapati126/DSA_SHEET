string=input() #Take input from user 
str_a=list(string) #convert string to list because we can't assign values on string
i=0
j=len(str_a)-1
while i<j:
    str_a[i],str_a[j]=str_a[j],str_a[i]
    i+=1
    j-=1
string=''#again convert list to string
for i in range(len(str_a)):
    string+=str_a[i]
print(string)