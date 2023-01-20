n_list = [int(input()) for _ in range(9)]
max = n_list[0]
for i in n_list:
    if i > max:
        max = i
print(max)
print(n_list.index(max)+1)


