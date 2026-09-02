# p=float(input("No of Units"))
# if(p==0>=100):
#     print("Your charge is ",p=p+5)
# elif(p<100<=300)
#     p=+7
# elif(p<=300<=2000)
#     p=+10
# elif(p<300<2000)
#     p=+0.5


# unit=(input("Select No of Units,press 1)  0-100, 2) 100-300, 3)300 & above :"))

# if(unit=='1'):
#    if(unit>100):
#        print("your charge is",unit+5)

# elif(unit=='2'):
#     p+7
# elif(p=='3'):
#     p+10
# else:
#     print("Invalid Statement")


print("\nBill rates 0-100 is 5rs, 100-300 is 7rs, 300-above is 10 ")
unit=int(input("\nEnter units:"))
if(unit<=100):
    print("\nAccording your Units, Rate lies 0-100,So charge is 5rs")
    bill=unit*5
    print(bill)
elif(unit<=300):
    print("\nAccording your Units,Rate lies 100-300,So charge is 7rs")
    bill=unit*7
    print(bill)
elif(unit<=2000):
    print("\nAccording your Units,Rate lies 300-above,So charge is 10rs")
    bill=unit*10
    print("\nbill charge according units range:",bill)
    if(bill>2000):
        surcharge=bill*0.05
        print("\nSurcharge is:",surcharge)
        print("\nYour bill is excedding 2000rs, Total is:",surcharge+bill)
else:
    print("INvalid")