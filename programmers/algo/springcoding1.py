# 스프링 코딩 1번

def solution(lotteries):
    answer = 0
    arr = []
    for i in range(len(lotteries)):
        num = lotteries[i][0] / (lotteries[i][1] + 1)
        if num >= 1 :
            num = 1
        arr.append([num, lotteries[i][2],i+1])

    print(arr)
    t = sorted(arr, key=lambda x: (-x[0], -x[1]))
    print(t)
    answer = t[0][2]
    return answer


lotteries = [[10, 19, 800], [20, 39, 200], [100, 199, 500]]
solution(lotteries)