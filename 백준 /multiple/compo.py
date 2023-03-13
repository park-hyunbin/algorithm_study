m = int(input())
n = int(input())

list  = []

for i in range(m,n+1):
    if i > 1 :
        for x in range(2,i):
            if i % x == 0:
                break
        else :
            list.append(i)

if len(list) > 0 :
    print(sum(list))
    print(min(list))
else :
    print(-1)

