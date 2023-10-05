
accountno = (input("enter a accountno"))
pin = (input("enter a pin"))
currentbalance = int(input("enter a currentbalance"))
withdraw = int(input("enter a withdraw amount"))
total = int(currentbalance) - int(withdraw)
#to check the curreentbalance is sufficent or not
if not(accountno) == (pin):
        print(" account and pin should not be match")
elif not(accountno.isnumeric() and pin.isnumeric()):
        print("enter a valid nos")
elif (withdraw) > currentbalance:
        print("amount is not sufficient")
#if suffi ent print the remainging amount
elif (total) <= currentbalance:
        print(total)
else:
    print(total)

#if user click on number

if(accountno) == (pin):
    n = int(input("enter the amount :"))
    #user click on 1 print withdraw amount
    if(n == 1):
        print(withdraw)
        #user click on 2 print total amount
    elif(n== 2):
            print(total)





