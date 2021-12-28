x = lambda a, b : b*a
print(x(2,3))

def f1(x):
    return lambda a: a*x
f2 = f1(2)
print(f2(5))