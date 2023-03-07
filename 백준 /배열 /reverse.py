n,m = map(int,input().split())
arr = [str (i+1) for i in range(n)]

for _ in range(m):
    i,j = map(int,input().split())
    arr[i-1:j] = arr[i-1:j][::-1]

print(*arr)