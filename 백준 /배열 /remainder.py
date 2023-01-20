import sys
input = sys.stdin.readline

n_list2 = []
n_list = [int(input()) for _ in range(10)]
for i in n_list:
    n_list2.append(i % 42)
n_list3 = []
for v in n_list2 :
    if v not in n_list3 :
        n_list3.append(v)
print(len(n_list3))
