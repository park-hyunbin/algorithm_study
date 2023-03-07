str = input()
list = []
word = str.split()
list.append(word)
count = 0
for _ in range(len(word)):
    for i in list :
        count += 1
print(count)
