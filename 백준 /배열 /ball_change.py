n,m = map(int,input().split())

arr = [str(i+1) for i in range(n)]

for i in range(m):
    x, y = map(int, input().split())
    arr[x-1] , arr[y-1] = arr[y-1], arr[x-1]

print(*arr)

