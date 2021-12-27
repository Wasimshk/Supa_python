print("welcome")
bal = 30000
pin=int(input("Enter the pin: "))
if pin==1234:
    t=int(input("1 - Cash withdraw\n2 - Balance Inquiry\n\tChoose the transaction: "))
    if t==1:
        w=int(input("Enter the amount: "))
        if w%100!=0:
            print("Amount needs to be multiple of 100")
        elif w>bal:
            print("Insufficiant Balance")
        elif w%100==0 and w<=bal:
            print("please collect your cash\n available balance is: ", bal-w)
            print("Thanks")
    elif t==2:
        print("avaialable balance is:", bal)
else:
    print("Invalid pin")
