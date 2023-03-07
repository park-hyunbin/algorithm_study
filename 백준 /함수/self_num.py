
def d(n):
    n = n+ sum(map(int,str(n)))
    return n

non_selfnum = []

for i in range(1,10001):
    non_selfnum.append( d(i) )

for i in range(1,10001):
    if i not in non_selfnum :
        print(i)