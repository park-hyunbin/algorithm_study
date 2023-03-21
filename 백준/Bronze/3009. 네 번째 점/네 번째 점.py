list_a = []
list_b = []
for _ in range(3):
    a,b = map(int,input().split())
    list_a.append(a)
    list_b.append(b)
for i in range(3) :
    if list_a.count(list_a[i]) == 1 :
        x = list_a[i]
    if list_b.count(list_b[i]) == 1 :
        y = list_b[i]

print(x,y)
