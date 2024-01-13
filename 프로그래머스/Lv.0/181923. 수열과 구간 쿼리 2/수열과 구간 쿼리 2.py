
2
3
4
5
6
7
8
9
10
11
12
13
def solution(arr, queries):
    answer = []
    for s,e,k in queries :
        mn = []
        for i in range(s,e+1) :
            if arr[i] > k :
                mn.append(arr[i])
        if len(mn) == 0 :
            answer.append(-1)
        else :
            answer.append(min(mn))
    return answer
