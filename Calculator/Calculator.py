# *************************************************************
# COMMAND LINE APPLICATION OF CALCULATOR

# Author  : Himi Patel
# For     : Internship (TASK-2)

# Description :
# This command-line application is used to perform basic arithmetic operations.
# It supports Addition, Subtraction, Multiplication, Division, Modulus,
# Floor Division, and Exponentiation (Power).
# Handles division by zero errors and invalid choices.
# ************************************************************

print("\n-------------------------------------------\n")
print("\t\t***CALCULATOR APP***")


def add(num1,num2):
    return num1+num2
        
def sub(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

def modulus(num1,num2):
    return num1%num2

def exponential(num1,num2):
    return num1**num2

def floor_division(num1,num2):
    return num1//num2



print("\nselect operation.")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.modulus")
print("6.exponentiation")
print("7.floor division")
print("8.exit")

while True:
    print("\n-------------------------------------------")
    choice=input("\nenter the operation you want to perform(1|2|3|4|5|6|7|8):")

    if choice not in ["1","2","3","4","5","6","7","8"]:
        print("Invalid choice. please select a valid operation.")
        continue

    if choice=="8":
            print("Thank you for using the calculator!")
            exit()

    try:
        num1=int(input("enter first number:"))
        num2=int(input("enter second number:"))
    
    except ValueError:
        print("Invalid input. please enter a number.")
        continue


   

    print("\n")
    if choice=="1":
        print(f"addition of  {num1} + {num2} = {add(num1,num2)}")

    elif choice=="2":
        print(f"subtraction of {num1} - {num2} = {sub(num1,num2)}")

    elif choice=="3":
        print(f"multiplication of {num1} * {num2} = {multiply(num1,num2)}")

    elif choice=="4":
          if num2==0:
            print("Error! division by zero\n")
          else:
            print(f"division of {num1} / {num2} = {divide(num1,num2)}")

    elif choice=="5":
        if num2==0:
            print("Error! division by zero\n")
        else:
            print(f"modulus of {num1} % {num2} = {modulus(num1,num2)}")

    elif choice=="6":
        print(f"exponentiation of {num1} ** {num2} = {exponential(num1,num2)}")

    elif choice=="7":
          if num2==0:
            print("Error! division by zero\n")
          else:
            print(f"floor division of {num1}//{num2} = {floor_division(num1,num2)}")

    else:
        print("Thank you for using the calculator!")
        exit()