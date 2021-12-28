num=int(input("Enter the number to get the factorial: "))
def factorial(x):
    my_fact=1
    for i in range(x): # variable under function and range should be same here X is same for function and the range
        my_fact=my_fact*(i+1)
    return my_fact
print("factorial of given number is:", factorial(num))