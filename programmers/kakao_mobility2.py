# 2번 문제
from collections import defaultdict

def solution(id_list, k):
    arr = defaultdict(int)
    for i in id_list:
        temp = set(i.split())
        print(temp)
        for j in temp:
            if arr[j] < k:
                arr[j] += 1

    answer = 0
    print(arr)
    return answer




id_list = ["A B C D", "A D", "A B D", "B D"]

k = 2

# ["JAY", "JAY ELLE JAY MAY", "MAY ELLE MAY", "ELLE MAY", "ELLE ELLE ELLE", "MAY"]
# k =3

print(solution(id_list, k))


#7
#8