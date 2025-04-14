
def add(num1,num2):
    return num1+num2
        
def sub(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    if num2==0:
        return "Error! division by zero"

    return num1/num2

def modulus(num1,num2):
    if num2==0:
        return "Error! division by zero"
        
    return num1%num2

def exponential(num1,num2):
    return num1**num2

def floor_division(num1,num2):
    if num2==0:
        return "Error! division by zero"
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
    print("\n------------------------------------------------------------------\n")
    choice=input("enter the operation you want to perform(1|2|3|4|5|6|7|8):")

    if choice not in ["1","2","3","4","5","6","7","8"]:
        print("Invalid choice. please select a valid operation.")
        exit()


    print("\n------------------------------------------------------------------\n")
    if choice=="8":
            print("Thank you for using the calculator!")
            exit()

    num1=int(input("enter first number:"))
    num2=int(input("enter second number:"))

    print("\n------------------------------------------------------------------\n")


    if choice=="1":
        print(f"addition of  {num1} + {num2} = {add(num1,num2)}")

    elif choice=="2":
        print(f"subtraction of {num1} - {num2} = {sub(num1,num2)}")

    elif choice=="3":
        print(f"multiplication of {num1} * {num2} = {multiply(num1,num2)}")

    elif choice=="4":
        print(f"division of {num1} / {num2} = {divide(num1,num2)}")

    elif choice=="5":
        print(f"modulus of {num1} % {num2} = {modulus(num1,num2)}")
    elif choice=="6":
        print(f"exponentiation of {num1} ** {num2} = {exponential(num1,num2)}")

    elif choice=="7":
        print(f"floor division of {num1}//{num2} = {floor_division(num1,num2)}")

    else:
        print("Thank you for using the calculator!")
        exit()