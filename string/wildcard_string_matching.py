

def f(i,j,wild,pattern,dp):
    if i<0 and j<0:
        return True
    if i<0 and j>=0:
        return False
    if j<0 and i>=0:
        for ii in range(i):
            if wild[i]!="*":
                return False
            return True
    if dp[i][j]!=-1:
        return dp[i][j]
    if (pattern[j]==wild[i] or pattern[i]=='?'):
        return dp[i][j]=f(i-1,j-1,wild,pattern,dp)
        
    
def match(wild,pattern):
    n=len(wild)
    m=len(pattern)
    dp=[[0 for _ in range(n)] for _ in range(m)]
    return f(n-1,m-1,wild,pattern,dp)