#Pattern Recognition
# Naïve Pattern Matching: tries every possible value of
# the shift s and checks whether it is a valid shift
# Complexity: O((n − m + 1)m) .
def naiveMatch(p,t): #find p in t
    if not p or not t:
        return 0
    m = len(p)
    n = len(t)
    found = False
    for i in range(n-m+1):
        j=0
        k=i
        while j < m and i < n and p[j]==t[k]:
            j+=1
            k+=1
        if j== m:
            print("Found valid shift", i, "for", p)
            found = True
        if not found:
            print("No match for",p)

#Examples
naiveMatch('aba','cbabababaa')
naiveMatch('abc','cbabababaa')
