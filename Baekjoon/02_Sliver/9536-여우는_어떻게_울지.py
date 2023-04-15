# 여우는 어떻게 울지?

T = int(input())

for i in range(T):
    sound = list(map(str, input().split()))
    while True:
        animal = list(map(str, input().split()))
        if animal[0] == "what":
            print(" ".join(sound))
            break
        while animal[2] in sound:
            sound.remove(animal[2])