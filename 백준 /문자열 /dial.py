n = list(input().lower())
alphabet = ["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]

time = 0

for i in n :
    for word in alphabet:
        if i in word:
            time += alphabet.index(word)+3
print(time)
