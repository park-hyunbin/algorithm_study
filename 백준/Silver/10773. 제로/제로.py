k = int(input())
list = []

for _ in range(k):
    i = int(input())
    if i == 0 :
        list.pop()
    else :
        list.append(i)

print(sum(list))