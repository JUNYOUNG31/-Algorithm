rc =[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
R = len(rc)
C = len(rc[0])




rc =[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
operations = ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]


from collections import deque

def solution(rc, operations):
    R = len(rc)
    C = len(rc[0])
    deque_rc = deque(rc)
    d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    if not "Rotate" in operations:
        for i in range((len(operations) % R)):
            deque_rc.appendleft(deque_rc.pop())
            answer = list(deque_rc)
            return answer


    for i in operations:
        if i == "ShiftRow":
            deque_rc.appendleft(deque_rc.pop())
        else:
            direct = 0
            x, y = 0, 1
            previous = deque_rc[0][0]
            while True:
                if x == 0 and y == 0:
                    deque_rc[0][0] = previous
                    break
                nx, ny = x + d[direct][0], y + d[direct][1]
                if nx < 0 or nx >= R or ny < 0 or ny >= C:
                    direct += 1
                    continue
                deque_rc[x][y], previous = previous, deque_rc[x][y]
                x, y = nx, ny
    answer = list(deque_rc)
    return answer