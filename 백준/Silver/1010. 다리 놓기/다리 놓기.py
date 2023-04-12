import math
t = int(input())
for _ in range(t) :
    n, m = map(int,input().split())
    if n == 0 or n == 1 :
        print(m)
    else :
        print(math.factorial(m) // (math.factorial(n) * math.factorial(m-n)))

