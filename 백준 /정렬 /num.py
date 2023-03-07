import sys
n = int(input())
data = [int(sys.stdin.readline()) for i in range(n)]
result = sorted(data)
for i in result :
    print(i)