
# Name="Pratik"
# Course="Python"`
# pay="Full-Payment"
# fees=40000
#make a program take detail from user name course mode of payment either full payment or installment
print("           ************    ")
Name=input("Enter Your Name:")
Course=input("\nEnter Your Course Opted:")
pay=input("\nPayment Mode: Full Payment OR Installment: ")
fees=int(input("\nEnter your Fees:"))

print("\n------------------RECIEPT------------------------")
print("\nName:", Name, end=" ")
print("          ", "Course:",Course)
print("Mode:",pay, end=" ")
print("    ","Fees:  ",fees)

print("\n--------------------------------------------------")

print(Course,end=" ")
print("                ",fees)
print("\n-------------------------------------------------- ")
print("Total:                 ",fees,)

print("  \n             ThankYou         ")
print("\n-------------------------------------------------- ")