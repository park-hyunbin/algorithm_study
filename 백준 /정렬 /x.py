import sys
input = sys.stdin.readline
n = int(input())
list = []
for _ in range(n):
    [a,b] = map(int,input().split())
    list.append([a,b])
list.sort()
for i in list :
    print(i[0],i[1])



