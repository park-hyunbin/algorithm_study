def solution(a, d, included):
    total_sum = 0
    for i in range(len(included)):
        num = a + i * d
        if included[i]:
            total_sum += num
    return total_sum
