# 이진 검색 트리
import sys

tree = []
for line in sys.stdin:
    tree.append(int(line))


def left_tree(start, end):
    if start > end:
        return
    check = end+1
    # 노드의 값보다 큰값의 idx 찾기
    for i in range(start+1, end+1):
        if tree[start] < tree[i]:
            check = i
            break

    # 루트의 왼쪽
    left_tree(start+1, check-1)
    # 루트의 오른쪽 
    left_tree(check, end)
    # 루트 노드를 출력
    print(tree[start])


left_tree(0, len(tree)-1)