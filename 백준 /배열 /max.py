N = int(input())
X = list(map(int,input().split()))
min = X[0]
max = X[0]
for i in X :
    if(min > i) :
        min = i
    elif (max < i) :
        max = i
print(min, max)