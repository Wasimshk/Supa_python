
l1 =[12,3,4,6,5,5,5,5,5,5,]
def count(x):
    count = 0
    for i in l1:
        if i == 5:
            count = count + 1
    return count
print("the count of the number 5 is:", count(l1))