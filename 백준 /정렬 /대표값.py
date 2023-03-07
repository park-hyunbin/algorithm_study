import sys
data = [int(sys.stdin.readline()) for i in range(5)]
sum = 0
for i in data :
    sum += i
    avg = sum//5

data.sort()
print(avg)
print(data[2])