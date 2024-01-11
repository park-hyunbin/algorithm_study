def solution(a, b, c):
    if a == b and b == c:
        answer = (a + b + c) * (a * a + b * b + c * c) * (a ** 3 + b ** 3 + c ** 3)
    elif a != b and b != c and c!= a :
        answer = a + b + c
    else:
        answer = (a + b + c) * (a ** 2 + b ** 2 + c ** 2)
    return answer
