n = int(input())
#6의 배수로 늘어남

line = 1
count = 1

while n > line :
        line += 6*count
        count+= 1
        continue
print(count)

