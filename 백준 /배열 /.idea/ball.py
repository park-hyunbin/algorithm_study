n,m = map(int,input().split())
arr = [0] *(n+1)
for _ in range(m):
    i,j,k = map(int,input().split())
    for l in range(i,j+1):
        arr[l]= k
for i in range(1,n+1):
    print(arr[i], end = " ")
