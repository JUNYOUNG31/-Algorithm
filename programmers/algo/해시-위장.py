# 위장

# 스파이들은 매일 다른 옷을 조합하여 입어 자신을 위장합니다.
# 예를 들어 스파이가 가진 옷이 아래와 같고 오늘 스파이가 동그란 안경, 긴 코트, 파란색 티셔츠를 입었다면
# 다음날은 청바지를 추가로 입거나 동그란 안경 대신 검정 선글라스를 착용하거나 해야 합니다.
# 종류	이름
# 얼굴	동그란 안경, 검정 선글라스
# 상의	파란색 티셔츠
# 하의	청바지
# 겉옷	긴 코트
# 스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.

def solution(clothes):
    answer = 1
    cnt = {}
    for i in clothes:  # 반복
        if i[1] in cnt:  # 만약  딕셔너리에 있다면
            cnt[i[1]] += 1  # value 1 증가
        else:  # 없으면
            cnt[i[1]] = 1  # 1
    print(cnt)

    for i in cnt.values():
        answer *= (i+1)
    return answer - 1






clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))