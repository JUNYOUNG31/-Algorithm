# N*M크기의 직사각형이 있다. 각 칸은 한 자리 숫자가 적혀 있다.
# 이 직사각형에서 꼭짓점에 쓰여 있는 수가 모두 같은 가장 큰 정사각형을 찾는 프로그램을 작성하시오.
# 이때, 정사각형은 행 또는 열에 평행해야 한다.

# 첫째 줄에 N과 M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다.
# 둘째 줄부터 N개의 줄에 수가 주어진다.

N , M = map(int, input().split())        # 가로세로 입력
box = []                                 # 리스트 변수 
Len_max = 0                              # 최대값의 길이
for _ in range(N):                       # N 만큼 반복     
    box.append(list(input()))        

for n in range(N):                       # 세로만큼 반복
    for m in range(M):                   # 가로만큼 반복
        for i in range(min(N,M)):        # i 번 반복인데 가로세로중 작은값까지만
            if n+i < N and m+i < M:
                if box[n][m] == box[n+i][m] == box[n][m+i] == box[n+i][m+i]:
            # N과 M의 인덱스 범위안에 있고, 4꼭지점의 값이 같을때
                    if Len_max < i:          # 최대값 바꾸기
                        Len_max = i          # 최대값의 인덱스 +1 해야 기존의 길이
                
print((Len_max+1)**2)                        # 넓이는 제곱