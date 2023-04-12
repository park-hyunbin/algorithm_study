import math
a,b,v = input().split()
a = int(a)
b = int(b)
v = int(v)
days = (v-b)/(a-b)
ans = math.ceil(days)

print(ans)
