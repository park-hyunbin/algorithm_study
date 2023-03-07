import sys
n = int(input())
data = [int(sys.stdin.readline()) for i in range(n)]
data.sort()

for i in data :
    print(i, end="\n")