word = input().upper()
word_list = list(set(word))

list = []

for i in word_list:
    result = word.count(i)
    list.append(result)


if list.count(max(list)) != 1:
    print("?")
else :
    print(word_list[list.index(max(list))])


#다시 풀어보기