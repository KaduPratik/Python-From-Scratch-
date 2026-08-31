# bal=10000

# print("\nWelcome to ATM Machine")
# que=input("\nPress 1.Check Balance, 2.Withdraw, 3.Deposit:")

# if(que=='1'):
#     print("\nYour Balance is:",bal)
# elif(que=='2'):
#     print("\nYour Balance is:",bal, end=" ")
#     wamt=float(input("Enter Your withdraw Amt:"))
#     if(bal>wamt):
#         bal=bal-wamt
#         print("Withdraw Sucessfull", end=" ")
#         print("Current balance:",bal)
# elif(que=='3'):
#     print("\nYour Balance is:",bal)
#     dep=float(input("How much you have to deposit:"))
#     if(dep>0):
#         bal+=dep
#         print("Sucessfully Deposit,Avaliavble Amount is:",bal)
#     else:
#         print("Deposit Amount should not Negative")
# else:
#     print("Invalid Process")

bal=1000

def CheckBalance(bal):
    print("\nYour Balance is:",bal)
def Withdraw(bal):
    print("\nYour Balance is:",bal, end=" ")
    wamt=float(input("Enter Your withdraw Amt:"))
    if(bal>wamt):
        bal=bal-wamt
        print("Withdraw Sucessfull", end=" ")
        print("Current balance:",bal)
    return bal
def Deposit(bal):
    print("\nYour Balance is:",bal)
    dep=float(input("How much you have to deposit:"))
    if(dep>0):
        bal+=dep
        print("Sucessfully Deposit,Avaliavble Amount is:",bal)
    else:
        print("Deposit Amount should not Negative")
    return bal
while(True):
    print("\nWelcome to ATM Machine")
    que=input("\nPress 1.Check Balance, 2.Withdraw, 3.Deposit:, 4.Exit :")

    if(que=='1'):
        CheckBalance(bal)
    elif(que=='2'):
        bal=Withdraw(bal)
    elif(que=='3'):
        bal=Deposit(bal)
    elif(que=='4'):
        break
    else:
        print("Invalid Process")









#if else, elif, nested elif ladder , scope 




# balance= 10000
# print("Initial balance:", balance)

# withdraw = float(input("Enter the amount to withdraw: "))
# if withdraw <= balance:
#     balance -= withdraw
#     print("Withdrawal successful.", end=" ")
#     #print("Remaining balance:", balance)

# else:
#     print("Insufficient balance. You cannot withdraw that amount.")
# print("Remaining balance:", balance)
