#lambda function


x = lambda a,b,c : a*b*c + 10
print(x(2,3,2))



def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

x = lambda a, b : a**b
print(x(2,3))

def myf(x):
    return lambda a,b : a**b-x
myf2 = myf(3)
print(myf2(2,3))