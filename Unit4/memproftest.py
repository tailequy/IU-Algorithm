from memory_profiler import profile
@ profile
def profileAnalysis():
    a = [0] * (10**7)
    b = a.copy()
    c = a[:]
    del c
    del b
    return a
if __name__ == '__main__':
    profileAnalysis()

#Command line
#python -m memory_profiler filename.py
#Plot the memory usage over time
#mprof run filename.py
#mprof plot