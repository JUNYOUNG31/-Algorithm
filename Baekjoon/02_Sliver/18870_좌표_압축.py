# 좌표 압축

# 수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.
# Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.
# X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.

# 첫째 줄에 N이 주어진다.
# 둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.

import sys

N = int(sys.stdin.readline())                       # 좌표수
X = list(map(int, sys.stdin.readline().split()))    # 좌표
X_sort = sorted(list(set(X)))                       # 중복값제거하고 정렬
X_dic = {}                                          # 딕셔너리 생성
for i in range(len(X_sort)):                        # 딕셔너리에 추가
    X_dic[X_sort[i]] = i                            # 인덱스를 추가해준다
for i in X:                                         # 반복해서
    print(X_dic[i], end=' ')                        # 인덱스 출력