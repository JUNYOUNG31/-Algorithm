# 럭비 클럽

while True:
    name, a, w = map(str, input().split())
    age = int(a)
    weight = int(w)
    if name == '#' and age == 0 and weight == 0:
        break
    if age > 17 or weight >= 80:
        print(name+' ' + 'Senior')
    else:
        print(name+' ' + 'Junior')