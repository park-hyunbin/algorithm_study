n = int(input())

arr = []

for _ in range(n):
    arr.append(list(input().split()))

arr.sort(key = lambda x: int(x[0]))

for i in arr :
    print(i[0], i[1])