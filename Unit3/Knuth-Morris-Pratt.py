#Knut-Moris-Pratt algorithm
#We pre-compute a prefix function in a table based on the pattern
# without knowledge of the text. Essentially, table[j]=k tells us
# that if the pattern fails to match at position j+1,
# we can assume that the first k characters
# of the pattern are already matched and proceed
# Complexity: KMP is ϴ(m + n)
def prefix(p):
    m = len(p) #size of pattern
    table = [0]*m #Creates a list of m zeros.
    i = 0
    for j in range(1,m):
        while i > 0 and p[i] != p[j]:
            i=table[i-1]
        if p[i] == p[j]:
            table[j] = i+1
        else:
            table[j]=i
    return table

#A call to prefix('abcabb') returns [0, 0, 0, 1, 2, 0].
# Here, Table[4] = 2 tells us that when a failure to match occurs at position 5
# of the pattern, as in our example, a prefix of the pattern of size two
# is matched up when the pattern is realigned.
def kmp(p,t):
    m = len(p) #size of pattern
    n =len(t)
    table=prefix(p)
    index = []
    j=0
    for i in range(n):
        while j > 0 and p[j] != t[i]:
            j=table[j-1]
        if(p[j] == t[i]):
            j+=1
        if j == m:
            index.append(i - (j - 1))
            print("Match found at",i-j+1)
            j = table[j - 1]
    return index
#Examples
kmp('aba','cbabababaa')
kmp('abc','abdabeabfabc')

