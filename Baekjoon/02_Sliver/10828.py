# 스택

# 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다.
# 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.
import sys                        # 시간초과....

N = int(sys.stdin.readline().rstrip()) # 명령수
stack = []                        # 스텍 리스트
for i in range(N):                # 명령만큼 반복
    order = list(sys.stdin.readline().rstrip().split()) # push 때문에 리스트화

    if order[0] == 'push':        # 첫번째 인덱스가 push 면
        stack.append(order[1])    # 1번째 인덱스를 스텍에 저장
    elif order[0] == 'pop':       # pop 명령
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif order[0] == 'size':      # size 명령
        print(len(stack))
    elif order[0] == 'empty':     # empty 명령
        if not stack:
            print(1)
        else:
            print(0)
    if order[0] == 'top':         # top 명령
        if not stack:
            print(-1)
        else:
            print(stack[-1])