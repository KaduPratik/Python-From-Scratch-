Day 04 – ATM Machine 💳🏧

Welcome to Day 04 of my Python From Scratch learning journey.

In this project, I created a simple ATM Machine program using Python. The program allows the user to check their balance, withdraw money, deposit money, and exit the ATM.

📌 Project Overview

This project demonstrates how basic Python concepts can be combined to create a simple interactive ATM system.

ATM Operations

The program provides four options:

💰 Check Balance
💸 Withdraw Money
💵 Deposit Money
🚪 Exit

The initial balance is set to ₹1000.

🧠 Concepts Learned

This project helped me practice the following Python concepts:

Variables
input()
print()
if, elif, and else
while loop
Functions
Function parameters
return statements
Updating variable values
Basic arithmetic operations
Conditional validation
Function scope

The project specifically uses separate functions for checking balance, withdrawing money, and depositing money.

⚙️ How It Works
1. Check Balance

The CheckBalance() function displays the user's current balance.

def CheckBalance(bal):
    print("\nYour Balance is:", bal)
2. Withdraw Money

The Withdraw() function asks the user for the withdrawal amount and updates the balance if sufficient funds are available.

def Withdraw(bal):
    wamt = float(input("Enter Your withdraw Amt:"))
    if bal > wamt:
        bal = bal - wamt
    return bal
3. Deposit Money

The Deposit() function accepts a deposit amount and adds it to the current balance.

def Deposit(bal):
    dep = float(input("How much you have to deposit:"))
    if dep > 0:
        bal += dep
    return bal
4. Exit

The program continuously displays the ATM menu using a while(True) loop until the user selects option 4.

🖥️ Example Menu
Welcome to ATM Machine

Press 1.Check Balance, 2.Withdraw, 3.Deposit:, 4.Exit :
Example
Press 1.Check Balance, 2.Withdraw, 3.Deposit:, 4.Exit : 1

Your Balance is: 1000

If the user withdraws money:

Press 1.Check Balance, 2.Withdraw, 3.Deposit:, 4.Exit : 2

Your Balance is: 1000 Enter Your withdraw Amt: 200
Withdraw Sucessfull Current balance: 800
🔄 Program Flow
Start
  ↓
Set Initial Balance
  ↓
Display ATM Menu
  ↓
Choose an Operation
  ↓
 ┌───────────────┬───────────────┬───────────────┬──────────┐
 ↓               ↓               ↓               ↓
Check          Withdraw        Deposit          Exit
Balance
 ↓               ↓               ↓               ↓
Display        Update          Update           Stop
Balance        Balance         Balance         Program
  └───────────────┴───────────────┴───────────────┘
                  ↓
             Show Menu Again
📚 Day 04 Topics
if
elif
else
Nested conditions
Conditional ladder
Functions
Function parameters
Return values
Variable scope
while loop

These topics are also reflected in the learning notes included with the Day 04 code.

🚀 Future Improvements

I can improve this ATM project by adding:

🔐 PIN authentication
💳 Multiple user accounts
💰 Minimum balance validation
🧾 Transaction history
🏦 Transfer money functionality
🔢 Daily withdrawal limits
⚠️ Better input validation
💾 File/database-based account storage
🎯 Learning Goal

The main goal of this project was to understand how functions, conditional statements, loops, parameters, and return values work together in a practical Python program.

🐍 Python From Scratch – Day 04

Project: ATM Machine
Language: Python
Level: Beginner
Focus: Functions, Conditions & Loops

⭐ If you find this project useful, consider giving the repository a star!
