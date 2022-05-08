




queue1 =[3, 2, 7, 2]

queue2 = 	[4, 6, 5, 1]

from collections import deque

def solution(queue1, queue2):
    answer = 0
    deque1 = deque(queue1)
    deque2 = deque(queue2)

    sum1 = sum(queue1)
    sum2 = sum(queue2)
    len1 = len(queue1)
    if (sum1+sum2) % 2 != 0:
        answer = -1
        return answer
    num = (sum1+sum2) // 2
    if sum1 == num:
        return answer
    for i in range(len1):
        if queue1[i] > num or queue2[i] > num:
            answer = -1
            return answer
        if queue1[i] == num or queue2[i] == num:
            answer = i*2 + len1 + 1
            return answer

    for i in range(len1):
        if sum1 > sum2:
            answer += 1
            temp = deque1.popleft()
            sum1 -= temp
            queue2.append(temp)
            sum2 += temp
        if sum1 < sum2:
            answer += 1
            temp = deque2.popleft()
            sum2 -= temp
            queue1.append(temp)
            sum1 += temp
        if sum1 == num:
            break
    else:
        answer = -1
    return answer


print(solution(queue1,queue2))