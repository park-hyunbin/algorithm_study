n,m = map(int,input().split())

arr = [i+1 for i in range(n)]

for _ in range(m):
    i,j,k = map(int, input().split())
    arr[i-1:j] = arr[k-1:j] + arr[i-1:k-1]

print(*arr)
