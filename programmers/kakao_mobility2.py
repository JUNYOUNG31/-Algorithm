# 2번 문제
from collections import defaultdict

def solution(id_list, k):
    arr = defaultdict(int)
    for i in id_list:
        temp = set(i.split())

        for j in temp:
            if arr[j] < k:
                arr[j] += 1

    answer = 0
    for i in arr:
        answer += arr[i]

    return answer




#id_list = ["A B C D", "A D", "A B D", "B D"]

#k = 2

id_list = ["JAY", "JAY ELLE JAY MAY", "MAY ELLE MAY", "ELLE MAY", "ELLE ELLE ELLE", "MAY"]
k =3

print(solution(id_list, k))


#7
#8