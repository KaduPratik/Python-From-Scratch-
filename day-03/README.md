❤️ DAY 3 of Learning Python 🐍
🧾 Admission Receipt Program

Welcome to Day 3 of my Python learning journey! 🚀

Today, I created an Admission Receipt Program using Python.

The program takes student admission details from the user and generates a simple receipt containing the student's name, course, payment mode, and fees.

📁 Program — admission_receipt.py
🧠 Concepts Covered
⌨️ Taking input using input()
📦 Using variables
🔢 Converting input into an integer using int()
🖨️ Printing formatted output using print()
📌 Using end in print()
🧾 Creating a simple receipt layout
💬 Using comments in Python
🔄 Working with user-provided data
🧑‍💻 Program
# Name = "Pratik"
# Course = "Python"
# pay = "Full-Payment"
# fees = 40000

# Make a program that takes details from the user:
# Name, Course, Mode of Payment (Full Payment or Installment), and Fees

print("           ****************    ")

Name = input("Enter Your Name:")

Course = input("\nEnter Your Course Opted:")

pay = input("\nPayment Mode: Full Payment OR Installment: ")

fees = int(input("\nEnter your Fees:"))

print("\n------------------RECIEPT------------------------")

print("\nName:", Name, end=" ")

print("          ", "Course:", Course)

print("Mode:", pay, end=" ")

print("    ", "Fees:  ", fees)

print("\n--------------------------------------------------")

print(Course, end=" ")

print("                ", fees)

print("\n-------------------------------------------------- ")

print("Total:                 ", fees)

print("  \n             ThankYou         ")

print("\n-------------------------------------------------- ")
📋 Example Input
Enter Your Name: Pratik

Enter Your Course Opted: Python

Payment Mode: Full Payment OR Installment: Full Payment

Enter your Fees: 40000
🧾 Example Output
------------------RECIEPT------------------------

Name: Pratik           Course: Python

Mode: Full Payment     Fees: 40000

--------------------------------------------------

Python                40000

--------------------------------------------------

Total:                 40000

             ThankYou

--------------------------------------------------
🔍 Key Learning
1. Taking User Input

The input() function is used to take information from the user.

Name = input("Enter Your Name:")
Course = input("Enter Your Course Opted:")
pay = input("Payment Mode: Full Payment OR Installment: ")
2. Converting Input to Integer

By default, input() returns a string.

Since fees are a numerical value, I converted the input into an integer using int().

fees = int(input("Enter your Fees:"))
3. Using end

The end parameter controls what happens at the end of a print() statement.

print("Name:", Name, end=" ")

Instead of moving immediately to a new line, the next output continues on the same line.

🚀 Day 3 Summary

Today I learned how to combine variables, user input, data type conversion, and print formatting to create a small practical Python program.

This program helped me understand how Python can be used to create simple real-world applications.

🐍 Learning Python one program at a time.

Day 3 complete! ❤️💻🚀

📈 Learning Journey
Day	Topic	Status
Day 1	Python Basics & First Program	✅ Completed
Day 2	Conditional Statements	✅ Completed
Day 3	User Input & Admission Receipt	✅ Completed
Day 4	Coming Soon...	🔜
👨‍💻 Author

Pratik

🐍 Learning Python | 💻 Building Skills | 🚀 Growing Every Day
