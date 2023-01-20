str1=input()
par=['(','{','[']

stack=[]
top=-1
if len(str)%2!=0:
    print(False)
for i in str1:
    if i not in par:
        stack.append(i)
        top+=1
    else:
        if i==')' and len(stack)!=0:
            if stack[top]=='(':
                stack.pop()
                top-=1
            else:
                print(False)
        elif i=='}' and len(stack)!=0:
            if stack[top]=='{':
                stack.pop()
                top-=1
            else:
                print(False)
        else:
            if len(stack)!=0  and stack[top]=='[':
                stack.pop()
                top-=1
            else:
                print(False)
if len(stack)==0:
    print(True)

        
            