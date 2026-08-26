print("hello world")

print("Hi, My name is Pratik and ") 
print("I am here to learn Python")

print("Hi, My name is Pratik and \nI am here to learn Python")

x=5
y=2
print("Value of x is",x)
print("Value of y is",y)

#print("Value of x is,x").  here x is inside  quotations so value of x is not printed

#print(a).  this is undefine error 

z= x+y
print("x+y =",z) #this is storing in diffrent value 

print("x+Y",x+y) # this storing in same print

print((x+y)*7)

# to reduce computation

z=x+y
print("x+y=",z)
print((z)*7)

a=int(input("x:")) # int= integer = datatype
# b=int(input("y:")) # float = decimal value
b=float(input("y:")) # float = decimal value

print("Addition of two values: ",a+b)
print("Substraction of two values: ",a-b)
print("Multiplication of two values: ",a*b)
print("power of two values: ",a**b)
print("Continous Division of two values: ",a/b) #0 nahi hota tab tak division
print("Modulus of two values: ",a%b) #percentage
print("Non Continous Division of two values: ",a//b)  


print("Addition of ",a,"and",b,":", a+b)



print("datatype of a:",type(a))
print("datatype of b:",type(b))

print(f"Addtion of {a} and {b} is {a+b
}") # f is for formatted string and {} are used for placeholder



emp_id =input("Enter your Employee id:")
name=input("Enter your name:")
print("Welcome",emp_id,name)


print("HI guys", end="|")
print("Welcome back to the python class")

x=input("Date:")
y=input("Month:")
z=input("Year:")

print("Date:",end="")
print(x,y,z,sep="/")

# name=input("Enert your Name:")
# print("Student Name",name,"a","x",sep="\t")
print("a",end=",")
print("b",end=",")
print("c")
