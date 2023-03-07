n, k = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
num.reverse()
print(num[k-1])

