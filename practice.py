a= "hello"
print(a[::-1]) #this means start from end and end when nothing left and move by 1 step

# Calculate the area of a circle

from math import pi

r=int(input("enter the radius of a circle: "))
print("the area of the circle with radius", r, "is:", pi*r**2)

# Write a Python program to count the number 4 in a given list.

def the_number(x):
    count=0
    for num in x:
        if num==4:
            count=count+1
    return count
print(the_number([4,6,4,6,4,6,8,4,86,4]))

# Write a Python program to calculate midpoints of a line.

print('\nCalculate the midpoint of a line :')

x1 = float(input('The value of x (the first endpoint) '))
y1 = float(input('The value of y (the first endpoint) '))

x2 = float(input('The value of x (the first endpoint) '))
y2 = float(input('The value of y (the first endpoint) '))

x_m_point = (x1 + x2)/2
y_m_point = (y1 + y2)/2

print( "The midpoint of the line is: ",(x_m_point,y_m_point))


# Filter the positive numbers from a list
nums = [34, 1, 0, -23, 12, -88]
print("Original numbers in the list: ",nums)
new_nums = list(filter(lambda x: x >0, nums))
print("Positive numbers in the said list: ",new_nums) 


# Empty a variable without destroying it
n = 20
d = {"x":200}
l = [1,3,5]
t= (5,7,8)
print(type(n)())
print(type(d)())
print(type(l)())
print(type(t)())

# print the table of given number 
num = int(input("enter the number to get the table: "))
for i in range(1,11):
    print(num, "X", i, "=", num*i)


#cleating classes and objects 


class Employee:
    pass 
emp1 = Employee()

emp1.name = "Wasims" # instance variable
print(emp1.name)

class employer:
    name = "CCtech" # class variable
emp1 = employer()
emp2 = employer()
emp2.name = "unknown"
print ("employer is", emp1.name)
print(emp2.name)

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





##############################################################################

s = "wasim"
print(s[::-1])


from math import pi
r = int(input("radius: "))
print("area of a cirle is: ", pi*r**2)


num= int(input("enter a number for the table: "))
for i in range(1,11):
    print(num, "X", i, "=", num*i)

class Employee:
    pass
emp1 = Employee()
emp2 = Employee()

emp1.name = "wasim"
emp1.age = 25

print(emp1.name)

class employer:
    name = "CCtech"
    field = "IT"
emp3 = employer()
emp4 = employer()
print(emp1.name)
print(emp2.field) # throws as error because using the attribute from the class employee

print(emp3.name)
print(emp4.field)


a = 2323
b = {"dawd","dwadd"}
c = [212,3224,545,1]
d = (54,"grg", 4)

print(type(c)())



s = "waim hdwhadhwa"
print(s[::-1])

from math import pi
r = 2
print(pi*r**2)

x1 = 2
x2 = 4
y1 = 2
y2 = 2

print(float(x1+ x2)/2, float(y1+ y2)/2)

l1 =[12,3,4,6,5,5,5,5,5,5,]
def count(x):
    count = 0
    for i in l1:
        if i == 5:
            count = count + 1
    return count
print( count(l1))

a = {"name" , "wasim", "age", 25}
print(type(a)())


a = 2
for i in range(1,11):
    print(a*i)


class Employee:
    pass 
emp1 = Employee()

emp1.name = "Wasims"
print(emp1.name)

class employer:
    name = "CCtech"
emp1 = employer()
print ("employer is", emp1.name)


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

print("welcome")
bal = 10000
PIN = int(input("enter pin: "))
if PIN == 1234:
    print("1 - withdraw\n2 - balance inquiry")
    t = int(input("choose the transaction: "))
    if t==1:
        w = int(input("enter the amout: "))
        if w %100!=0:
            print( "enter multiple of 100")
        elif w>bal:
            print("insufficiant amount")
        elif w%100==0 and w<=10000:
            print("collect your Cash\nyour available balance is", bal-w, "\n\tThank you")
    elif t==2:
        print("your balance is:", bal)  
    else:
        print("invalid input")
else:
    print("Wrong Pin")
    

fact= int(input("number: "))
def fact1(x):
    fact = 1
    for i in range(x):
        fact = fact*(i+1)
    return fact
print(fact1(fact))

# for i in range(100)[5:51:5]:

#     print(i)



x = lambda a,b : a+b
print(x(5,5))

def myf(x):
    return lambda a : a*x

myf2= myf(3)
print(myf2(5))



x = lambda a, b : a**b
print(x(2,3))

def myf(x):
    return lambda a,b : a**b-x
myf2 = myf(3)
print(myf2(2,3))




x = lambda a,b : b**a
print(x(2,3))

def myf(x):
    return lambda a,b : b*a*x
myf2 = myf(2)
print(myf2(2,2))




s = "wasim"
print(s[::-1])

r=2
from math import pi
print(pi*r*2)

x1,y1,x2,y2 = 2,2,4,4

x3=float(x1+x2)/2
y3=float(y1+y2)/2
print("the mid pt is:", (x3,y3))

s={2,3,1,5,4}
print(type(s)())

n = int(input("enter the num"))
for i in range(1,11):
    print(n,"X",i,"=", i*n)

for i in range(0, 51, 5):
    if i == 0:
        continue
    print(i)

for i in range(51)[:1:-5]:
    print(i)

class employee:
    pass
emp1=employee()
emp1.name = "Wasimsssss"

print(emp1.name)

class emp:
    name = 100
emp1=emp()
print(emp1.name)

x = lambda a,b: a*b
print(x(2,3))

def f1(x):
    return lambda a,b : (b-a)*x
f2 = f1(2)
print(f2(2,3))


import random
rr = random.sample(range(1,20), 5)

def min(x):
    min = rr[0]
    for i in rr:
        if i < min:
            min = i
    return min
print(min(rr))

def min_max(x):
    min = rr[0]
    max =rr[0]
    for i in rr:
        if i < min: 
            min =i
        if i>max:
            max = i
    return (min, max)
print(min_max(rr))

n = len(rr)

def mean(x):
    sum=0
    for i in range(0, n):
        sum = sum+rr[i]
    return sum/n
print(mean(rr))

rr.sort()

def median(x):
    if n%2==0:
        m1 = rr[n//2]
        m2 = rr[n//2-1]
        m = (m1+m2)/2
    else:
        m = rr[n//2]
    return m
print(median(rr))

ee = [12,32,54,65,1,2,2,2,2,2,2,2]
def count(X):
    count=0
    if i ==2:
        count = count +1
    return count
print(count(ee))

ff=5
def fact(x):
    f=1
    for i in range(x):
        f=f*(i+1)
    return f
print(fact(ff))

x = lambda a, b : b*a
print(x(2,3))

def f1(x):
    return lambda a: a*x
f2 = f1(2)
print(f2(5))