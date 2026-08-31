❤️ DAY 4 of Learning Python 🐍 💳 ATM Machine using Functions

Welcome to Day 4 of my Python learning journey! 🚀

Today, I created a simple ATM Machine program using Python.

This project helped me understand how functions, parameters, return values, conditional statements, loops, and variable scope work together to create an interactive program.

The ATM allows the user to:

💰 Check Balance
💸 Withdraw Money
💵 Deposit Money
🚪 Exit the ATM

🧠 What I Learned Today

Today I practiced:

Creating functions using def
Passing values to functions using parameters
Returning updated values using return
Calling functions
Using if, elif, and else
Using a while loop
Updating variable values
Performing arithmetic operations
Taking user input using input()
Converting input using float()
Understanding variable scope
Building a menu-driven Python program
🔹 1. Initial Balance

The ATM starts with an initial balance.

bal = 1000

This variable stores the current balance of the user.

As money is withdrawn or deposited, the value of bal changes.

🔹 2. Creating Functions

Instead of writing all the ATM operations in one place, I created separate functions for each operation.

The three main functions are:

CheckBalance()
Withdraw()
Deposit()

This makes the program easier to understand and organize.

🔹 3. Check Balance Function

The CheckBalance() function displays the current balance.

def CheckBalance(bal):
    print("\nYour Balance is:", bal)

The balance is passed to the function using the parameter bal.

When the user selects option 1, the function is called:

CheckBalance(bal)
💡 Important Learning

A function can receive a value through a parameter.

bal
 ↓
CheckBalance(bal)
 ↓
Display Balance
🔹 4. Withdraw Function

The Withdraw() function allows the user to withdraw money.

def Withdraw(bal):
    print("\nYour Balance is:", bal, end=" ")
    wamt = float(input("Enter Your withdraw Amt:"))

    if bal > wamt:
        bal = bal - wamt
        print("Withdraw Sucessfull", end=" ")
        print("Current balance:", bal)

    return bal
🧠 How it works

First, the current balance is displayed.

Then the user enters the withdrawal amount:

wamt = float(input("Enter Your withdraw Amt:"))

The program checks whether there is enough balance:

if bal > wamt:

If the condition is true:

bal = bal - wamt

The withdrawal amount is deducted from the balance.

Finally, the updated balance is returned:

return bal
🔄 Why return bal is Important

This was an important learning point.

Inside the function, the balance gets updated.

bal = bal - wamt

But the updated value needs to be sent back to the main program.

Therefore:

return bal

And when calling the function:

bal = Withdraw(bal)

The updated balance is stored again in bal.

Program Flow
Current Balance
       ↓
Withdraw Function
       ↓
Enter Withdrawal Amount
       ↓
Is Balance Greater Than Amount?
      ↙              ↘
    YES               NO
     ↓                 ↓
Deduct Amount      No Update
     ↓
Return New Balance
     ↓
Update bal
🔹 5. Deposit Function

The Deposit() function allows the user to add money to the account.

def Deposit(bal):
    print("\nYour Balance is:", bal)
    dep = float(input("How much you have to deposit:"))

    if dep > 0:
        bal += dep
        print("Sucessfully Deposit,Avaliavble Amount is:", bal)
    else:
        print("Deposit Amount should not Negative")

    return bal

The user enters the deposit amount:

dep = float(input("How much you have to deposit:"))

The program checks whether the amount is greater than zero:

if dep > 0:

If the amount is valid:

bal += dep

The deposit is added to the balance.

The updated balance is then returned:

return bal
💡 Understanding bal += dep

This:

bal += dep

is a shorter way of writing:

bal = bal + dep

Similarly:

bal -= wamt

means:

bal = bal - wamt

These are called assignment operators.

🔹 6. Using a while Loop

The ATM should continue working until the user chooses Exit.

For this, I used:

while(True):

This creates a loop that keeps running continuously.

Inside the loop, the ATM menu is displayed:

print("\nWelcome to ATM Machine")
que = input("\nPress 1.Check Balance, 2.Withdraw, 3.Deposit:, 4.Exit :")

The user can select an operation again and again.

🔹 7. Using if, elif, and else

The user's choice is checked using conditional statements.

if(que == '1'):
    CheckBalance(bal)

elif(que == '2'):
    bal = Withdraw(bal)

elif(que == '3'):
    bal = Deposit(bal)

elif(que == '4'):
    break

else:
    print("Invalid Process")
🧠 How it works

The program checks the user's choice from top to bottom.

User Choice
     ↓
Is it 1?
 ↙       ↘
YES       NO
 ↓         ↓
Balance   Is it 2?
           ↙    ↘
         YES     NO
          ↓       ↓
      Withdraw   Is it 3?
                  ↙    ↘
                YES     NO
                 ↓       ↓
              Deposit  Is it 4?
                       ↙    ↘
                     YES     NO
                      ↓       ↓
                     Exit   Invalid
🔹 8. Using break

When the user selects option 4, the program should stop.

For this, I used:

elif(que == '4'):
    break

The break statement immediately stops the loop.

So the ATM program exits.

🔹 9. Function Parameters

One important concept I practiced today was function parameters.

For example:

def Withdraw(bal):

Here, bal is a parameter.

When the function is called:

Withdraw(bal)

the current balance is passed into the function.

Main Program
     ↓
   bal
     ↓
Withdraw(bal)
     ↓
Function receives balance
🔹 10. Return Values

Another important concept was the return statement.

The Withdraw() function returns the updated balance:

return bal

Then the main program stores that returned value:

bal = Withdraw(bal)

The same concept is used for deposits:

bal = Deposit(bal)
💡 Key Learning
Function
   ↓
Calculate / Update
   ↓
return value
   ↓
Main Program
   ↓
Update variable
🖥️ Example Output
When the user checks balance
Welcome to ATM Machine

Press 1.Check Balance, 2.Withdraw, 3.Deposit:, 4.Exit : 1

Your Balance is: 1000
When the user withdraws money
Press 1.Check Balance, 2.Withdraw, 3.Deposit:, 4.Exit : 2

Your Balance is: 1000 Enter Your withdraw Amt: 200

Withdraw Sucessfull Current balance: 800
When the user deposits money
Press 1.Check Balance, 2.Withdraw, 3.Deposit:, 4.Exit : 3

Your Balance is: 800
How much you have to deposit: 500

Sucessfully Deposit,Avaliavble Amount is: 1300
When the user enters an invalid choice
Press 1.Check Balance, 2.Withdraw, 3.Deposit:, 4.Exit : 7

Invalid Process
🔄 Complete ATM Program Flow
Start
  ↓
Set Initial Balance = 1000
  ↓
Display ATM Menu
  ↓
Choose Operation
  ↓
 ┌─────────────┬─────────────┬─────────────┬─────────┐
 ↓             ↓             ↓             ↓
Check        Withdraw      Deposit        Exit
Balance         ↓             ↓             ↓
 ↓             Update        Update        Stop
Display        Balance       Balance       Program
Balance           └──────┬──────┘
                         ↓
                   Show Menu Again
📚 Day 4 Topics
Topic	What I Practiced
if	Checking conditions
elif	Checking multiple choices
else	Handling invalid choices
while loop	Repeating the ATM menu
Functions	Separating ATM operations
Parameters	Passing balance to functions
return	Returning updated balance
Variables	Storing balance and input
float()	Converting money input
Arithmetic	Adding and subtracting money
Scope	Understanding variables inside functions
🎯 What I Built Today

Today I built a simple ATM Machine in Python with:

💰 Balance Checking
💸 Money Withdrawal
💵 Money Deposit
🚪 Exit Option
🔄 Continuous Menu
⚙️ Separate Functions
✅ Basic Input Validation

This project helped me understand how different Python concepts can work together in a real-world style program.

🚀 Future Improvements

I can improve this ATM project by adding:

🔐 PIN Authentication
👤 Multiple User Accounts
💰 Minimum Balance Validation
🧾 Transaction History
🏦 Money Transfer
🔢 Daily Withdrawal Limits
⚠️ Better Input Validation
💾 File/Database-Based Account Storage

❤️ Day 4 Summary

Today I learned that functions can make a Python program more organized and reusable.

I practiced:

Functions → Organize the program
Parameters → Pass data into functions
return → Send data back
if/elif/else → Make decisions
while → Repeat the program
break → Exit the loop

The biggest learning from today's project was understanding how a function can receive a value, modify it, return it, and update the original variable.

🐍 Learning Python one concept at a time.

Day 4 complete! ❤️💻🚀

📈 Learning Journey
Day	Topic	Status
Day 1	Python Basics & First Program	✅ Completed
Day 2	Conditional Statements	✅ Completed
Day 3	Practice & Concepts	✅ Completed
Day 4	ATM Machine using Functions	✅ Completed
Day 5	Coming Soon...	🔜
👨‍💻 Author

Pratik

🐍 Learning Python | 💻 Building Skills | 🚀 Growing Every Day
