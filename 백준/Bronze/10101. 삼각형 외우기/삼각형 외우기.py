list = []
for i in range(3):
    angle = int(input())
    list.append(angle)

if list[i] == 60 :
    print("Equilateral")
elif list[0]+ list[1] + list[2] == 180 and len(set(list)) == 2:
    print("Isosceles")
elif list[0]+list[1]+list[2] == 180 and len(set(list)) == 3:
    print("Scalene")
else :
    print("Error")
