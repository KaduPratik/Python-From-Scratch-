❤️ DAY 5 of Learning Python 🐍 ⚡ Electricity Bill Calculator

Welcome to Day 5 of my Python learning journey! 🚀

Today, I practiced Conditional Statements and Arithmetic Operations by creating a simple Electricity Bill Calculator in Python.

The program takes the number of units from the user and calculates the electricity bill based on different unit ranges.

It also checks whether the bill exceeds ₹2000 and applies a 5% surcharge.

This was a good practice of using if, elif, else, arithmetic operations, user input, and nested conditions together.

🧠 What I Learned Today

Today I practiced:

Taking user input using input()
Converting input using int()
Using if statements
Using elif statements
Using else statements
Working with multiple conditions
Performing multiplication calculations
Calculating a percentage
Using a nested if statement
Comparing values using >
Storing calculated values in variables
Building a real-world billing program
Understanding how conditions control program flow
🔹 1. Taking User Input

First, the program displays the electricity billing rates:

print("\nBill rates 0-100 is 5rs, 100-300 is 7rs, 300-above is 10 ")

Then the user enters the number of units:

unit = int(input("\nEnter units:"))
💡 Why use int()?

The input() function normally returns data as a string.

For example:

"100"
"250"
"500"

Using:

int(input())

converts the input into an integer.

So:

"100" → 100
"250" → 250

This allows us to perform mathematical calculations.

🔹 2. Using if for 0–100 Units

The first condition checks whether the units are less than or equal to 100.

if(unit <= 100):
    print("\nAccording your Units, Rate lies 0-100,So charge is 5rs")
    bill = unit * 5
    print(bill)

If the user enters:

50

The condition:

unit <= 100

is True.

Therefore, the rate is ₹5 per unit.

Calculation
Units = 50
Rate = ₹5

Bill = 50 × 5
     = ₹250
🔹 3. Using elif for 100–300 Units

The second condition is:

elif(unit <= 300):
    print("\nAccording your Units,Rate lies 100-300,So charge is 7rs")
    bill = unit * 7
    print(bill)

If the first condition is false and the units are less than or equal to 300, this condition runs.

For example:

Units = 200
Rate = ₹7

Bill = 200 × 7
     = ₹1400
🔹 4. Using elif for 300–2000 Units

The next condition is:

elif(unit <= 2000):
    print("\nAccording your Units,Rate lies 300-above,So charge is 10rs")
    bill = unit * 10
    print("\nbill charge according units range:",bill)

If the previous conditions are false and the units are less than or equal to 2000, the program uses a rate of ₹10 per unit.

For example:

Units = 500
Rate = ₹10

Bill = 500 × 10
     = ₹5000
🔹 5. Nested if for Surcharge

Today I also practiced a nested if statement.

Inside the elif block, the program checks whether the calculated bill is greater than ₹2000.

if(bill > 2000):
    surcharge = bill * 0.05
    print("\nSurcharge is:", surcharge)
    print("\nYour bill is excedding 2000rs, Total is:", surcharge + bill)
🧠 How it works

First:

bill > 2000

checks whether the bill exceeds ₹2000.

If it does, the program calculates a 5% surcharge.

surcharge = bill * 0.05
💡 Understanding 5%

The decimal value:

0.05

represents:

5 / 100 = 5%

For example:

Bill = ₹5000

Surcharge = 5000 × 0.05
          = ₹250

Then:

Total Bill = Bill + Surcharge
           = ₹5000 + ₹250
           = ₹5250
🔄 Program Flow
Start
  ↓
Enter Units
  ↓
Are units <= 100?
  ↙           ↘
YES            NO
 ↓              ↓
Rate ₹5      Are units <= 300?
 ↓              ↙          ↘
Bill           YES          NO
                ↓            ↓
             Rate ₹7     Are units <= 2000?
                ↓            ↙          ↘
              Bill         YES          NO
                             ↓            ↓
                          Rate ₹10     Invalid
                             ↓
                           Bill
                             ↓
                       Is Bill > ₹2000?
                          ↙       ↘
                        YES        NO
                         ↓          ↓
                    5% Surcharge   Finish
                         ↓
                    Total Bill
                         ↓
                       Finish
🔹 6. Using else

Finally, the program uses else:

else:
    print("INvalid")

This handles values that do not satisfy any of the previous conditions.

🧪 Example Outputs
When user enters 50 units
Bill rates 0-100 is 5rs, 100-300 is 7rs, 300-above is 10

Enter units: 50

According your Units, Rate lies 0-100,So charge is 5rs
250
When user enters 200 units
Enter units: 200

According your Units,Rate lies 100-300,So charge is 7rs
1400
When user enters 500 units
Enter units: 500

According your Units,Rate lies 300-above,So charge is 10rs

bill charge according units range: 5000

Surcharge is: 250.0

Your bill is excedding 2000rs, Total is: 5250.0
📚 Key Concepts Practiced
Concept	What I Practiced
input()	Taking units from the user
int()	Converting input into integer
if	Checking the first unit range
elif	Checking additional ranges
else	Handling invalid values
*	Calculating the bill
>	Checking whether bill exceeds ₹2000
0.05	Calculating 5% surcharge
Nested if	Checking surcharge inside a condition
Variables	Storing units, bill and surcharge
📝 Important Learning

Today I understood how multiple conditions can be combined to solve a real-world problem.

For example:

if(unit <= 100):

checks the first range.

elif(unit <= 300):

checks the next range.

elif(unit <= 2000):

checks another range.

And finally:

else:

handles everything else.

The program evaluates the conditions from top to bottom.

🎯 What I Built Today

Today I created an:

⚡ Electricity Bill Calculator

The program can:

📥 Take units from the user
🔢 Convert input into an integer
⚡ Select a billing rate
🧮 Calculate the bill
💰 Calculate a 5% surcharge
📊 Calculate the final amount
❌ Handle invalid input

This small project helped me understand how Python conditions can be used to build practical programs.

🚀 Day 5 Summary

Today I learned how to combine:

input()
   ↓
int()
   ↓
if / elif / else
   ↓
Arithmetic Calculation
   ↓
Nested if
   ↓
Percentage Calculation
   ↓
Final Result

The biggest learning from today's practice was understanding how conditional statements can be used to divide a problem into different cases and perform different calculations for each case.

🐍 Learning Python one concept at a time.

Day 5 complete! ❤️💻⚡🚀

📈 Learning Journey
Day	Topic	Status
Day 1	Python Basics & First Program	✅ Completed
Day 2	Conditional Statements	✅ Completed
Day 3	Practice & Concepts	✅ Completed
Day 4	Functions & ATM Machine	✅ Completed
Day 5	Electricity Bill Calculator	✅ Completed
Day 6	Coming Soon...	🔜
👨‍💻 Author

Pratik

🐍 Learning Python | 💻 Building Skills | 🔥 Building the Habit | 🚀 Growing Every Day
