def solution(l, r):
    result_list = []

    for n in range(l, r + 1) :
        if all(digit in ['0', '5'] for digit in str(n)) :
            result_list.append(n)

    if not result_list:
        result_list.append(-1)

    return result_list