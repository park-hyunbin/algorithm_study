x,y,w,h = input().split()
x = int(x)
y = int(y)
w = int(w)
h = int(h)


print(min(x,y,h-y,w-x))