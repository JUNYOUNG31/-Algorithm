# 단속카메라

# 고속도로를 이동하는 모든 차량이 고속도로를 이용하면서 단속용 카메라를 한 번은 만나도록 카메라를 설치하려고 합니다.
# 고속도로를 이동하는 차량의 경로 routes가 매개변수로 주어질 때, 모든 차량이 한 번은 단속용 카메라를 만나도록 하려면
# 최소 몇 대의 카메라를 설치해야 하는지를 return 하도록 solution 함수를 완성하세요.

def solution(routes):
    answer = 1
    a = sorted(routes, key=lambda x:x[1])       # 나가는 지점을 기준으로 정렬
    i = 0                                       # 처음 
    j = 1                                       # 그다음 차
    # print(a)
    while j < len(routes):                      # 돌려서
        if a[i][1] < a[j][0]:                   # 처음차의 나가는 곳이 그다음차의 진입로 보다 작으면
            answer += 1                         # 1씩 추가
            i = j                               # 그리고 갱신
        j += 1                                  # 크다면 같은 카메라를 볼수있으니깐 다음차로 패스
        print(answer)
        print(i, j)
    return answer


routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]

print(solution(routes))