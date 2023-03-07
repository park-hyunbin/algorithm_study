word = list(input())
alphabet = [chr(i) for i in range(97,123)]

for i in alphabet:
    if i in word:
        print(word.index(i), end=" ")
    else :
        print("-1", end=" ")
