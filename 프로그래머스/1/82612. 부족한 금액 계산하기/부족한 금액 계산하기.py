def solution(price, money, count):
    ride = 0
    for _ in range(1, count+1):
        ride += price * _ 
    sum = money - ride
    answer = 0 if sum >= 0 else -sum
    return answer
