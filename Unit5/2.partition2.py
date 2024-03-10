#Imperative Programming
def partition(L,p):
    i=0
    j=len(L)-1
    while True:
        while (i <= j) and (L[i] <= p):
            i+=1
        while (i <=j) and (L[j] > p):
            j-=1
        if(i <= j):
            L[i],L[j] = L[j],L[i]
        else:
            break
    L[j], L[0] = L[0], L[j]
    return L
aList=[11,59,26,17,2,1,25,9,3,15]
print(partition(aList,11))