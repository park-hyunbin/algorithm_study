n = int(input())
n_list = list(map(int,input().split()))
max = n_list[0]

for i in n_list :
    if i > max :
        max = i

n_list2 = []
for i in n_list:
    n_list2.append(i/max*100)

sum = 0

for i in n_list2:
    sum += i
    ans = sum / len(n_list)
print(ans)
