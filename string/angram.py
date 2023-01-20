s=input("Enter String 1:")
t=input("Enter String 2:")
s=s.lower()
t=t.lower()
def isAnagram(s,t):
    hs={}
    for i in range(len(s)):
        if s[i] not in hs:
            hs[s[i]]=1
        else:
            hs[s[i]]+=1
    for i in range(len(t)):
        if t[i] not in hs:
            return False
        else:
            hs[t[i]]-=1
    for i in hs.values():
        if i!=0:
            return False
    return True

print(isAnagram(s,t))
        