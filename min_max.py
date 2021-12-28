import random
randl = random.sample(range(1,20), 6)
print(randl)

def min(x):
    min = randl[0]
    for i in randl:
        if i < min:
            min = i
    return min
print("min:", min(randl))

def max(x):
    max = randl[0]
    for i in randl:
        if i > max:
            max = i
    return max
print("max:", max(randl))

def min_max(x):
    min = randl[0]
    max= randl[0]
    for i in randl:
        if i < min:
            min =i
        elif i> max:
            max = i
    return min,max
print("min, max:", min_max(randl))