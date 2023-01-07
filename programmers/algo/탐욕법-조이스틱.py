# 조이스틱

# 조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.
# ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA
# 조이스틱을 각 방향으로 움직이면 아래와 같습니다.

def solution1(name):
    answer = 0
    list_name = list(name)
    updown = []
    left = -1
    right = 1
    # print(list_name)
    for i in range(len(list_name)):
        updown.append(min(ord(name[i]) - ord('A'), (ord('Z') - ord(name[i]) + 1)))
    print(updown)
    answer += sum(updown)
    # if 'A' in list_name:
    # for i in range(len(list_name)//2):
    return answer


def solution(name):
    answer = 0
    name = list(name)
    index = 0
    while 1:
        right = 1
        left = 1
        if name[index] != 'A':
            answer += min(ord(name[index])-ord('A'), (ord('Z')-ord(name[index])+1))
        name[index] = 'A'
        if name == ["A"]*len(name):
            break
        for i in range(1, len(name)):
            if name[index+i] == "A":
                right += 1
            else:
                break
        for i in range(1, len(name)):
            if name[index-i] == "A":
                left += 1
            else:
                break
        if right > left:
            answer += left
            index -= left
        else:
            answer += right
            index += right
    return answer


name = "JEROEN"
# name = "JAN"

print( solution(name))


