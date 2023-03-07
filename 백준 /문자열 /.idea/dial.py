alphabet = input()

time = 0

for i in alphabet:
    if i in ["a","b","c"] :
        time += 3
    elif i in ["d","e","f"] :
        time += 4
    elif alphabet in ["g","h","i"] :
        time += 5
    elif alphabet in ["j","k","l"] :
        time += 6
    elif alphabet in ["m","n","o"] :
        time += 7
    elif alphabet in ["p","q","r","s"] :
        time += 8
    elif alphabet in ["t","u","v"]:
        time += 9
    elif alphabet in ["w","x","y","z"]:
        time += 10

print(time)
