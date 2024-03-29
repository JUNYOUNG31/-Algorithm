# 베스트 앨범

# 스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다.
# 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.
# 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
# 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
# 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
# 노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때,
# 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.


def solution(genres, plays):
    answer = []
    genre = {}
    for i in range(len(genres)):
        if genres[i] in genre:  # 만약  딕셔너리에 있다면
            genre[genres[i]][i] = plays[i]  # value 1 증가
        else:  # 없으면
            genre[genres[i]] = {i: plays[i]}
    print(genre)
    genre_sort = {}
    for i, j in genre.items():
        genre_sort[i] = sorted(genre[i].items(), reverse=True, key=lambda x: x[1])
    print(genre_sort)
    hap = {}
    for i, j in genre.items():
        # print(i)
        hap[i] = 0
        for k in j.values():
            # print(k)
            hap[i] += k
    print(hap)
    hap_sort = sorted(hap.items(), reverse=True, key=lambda x: x[1])
    print(hap_sort)
    for i in range(len(hap_sort)):
        for j, k in genre_sort.items():
            if hap_sort[i][0] == j:
                # print(k)
                for l in k[:2]:
                    # print(l)
                    answer.append(l[0])

    return answer





genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

# print(solution(["A", "A", "B", "A", "B", "B", "A", "A", "A", "A"],  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
print(solution(genres, plays))