# 개표

V = int(input())
arr = list(str(input()))

if arr.count("A") > arr.count("B"):
    print("A")
elif arr.count("A") < arr.count("B"):
    print("B")
elif arr.count("A") == arr.count("B"):
    print("Tie")