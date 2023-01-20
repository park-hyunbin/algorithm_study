import sys
input = sys.stdin.readline

n_list = [int(input()) for _ in range(28)]
n_list2 = []
for i in range(1,31):
    n_list2.append(i)

n_list3 = []
for i in n_list2 :
    if i not in n_list:
        n_list3.append(i)

print(n_list3[0])
print(n_list3[1])
