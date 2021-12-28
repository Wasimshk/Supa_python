import random 
randl = random.sample(range(1, 20), 5)
print(randl)

def max(x):
    max = randl[0]
    for i in randl:
        if i > max:
            max =  i
    return max
print(max(randl))

def min(x):
    min = randl[0] 
    for i in randl:
        if i < min:
            min = i
    return min
print( min(randl))

def min_max(x):
    min = randl[0]
    max = randl[0]
    for i in randl:
        if i< min:
            min = i
        if i>max:
            max = i
    return (min, max)
print( min_max(randl))

n = len(randl)

def mean(x):
    sum=0
    for i in range(0,n):
        sum= sum + randl[i]
    return sum/n
print( mean(randl))

randl.sort()

def median(x):
    if n%2==0:
        median1 = randl[n//2]
        median2 = randl[n//2-1]
        median = (median1+median2)/2
    else: 
        median = randl[n//2]
    return median 
print(median(randl))
