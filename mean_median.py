import random
randl = random.sample(range(1,20), 6)
print(randl)

n= len(randl)
def mean(x):
    sum=0
    for i in range(0, n):
        sum =sum+ randl[i]
    return sum/n
print("mean:", mean(randl))


randl.sort()
def median(x):
    if n%2==0:
        median1=randl[n//2]
        median2=randl[n//2-1]
        median=(median1+median2)/2
    else:
        median=randl[n//2]
    return median
print("median:", median(randl))