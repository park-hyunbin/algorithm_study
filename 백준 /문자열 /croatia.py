word = input()
cro = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]


for i in cro :
    word = word.replace(i,'*')
print(len(word))



