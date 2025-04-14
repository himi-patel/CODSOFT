print("select operation.")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
print("5.exit")

choice=input("enter the operation you want to perform(1|2|3|4|5):")

if choice=="5":
        print(exit())

num1=int(input("enter first number:"))
num2=int(input("enter second number:"))


def add(num1,num2):
    return num1+num2
    
def substract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

if choice=="1":
    print(num1,"+",num2,"=",add(num1,num2))

elif choice=="2":
    print(num1,"-",num2,"=",substract(num1,num2))

elif choice=="3":
    print(num1,"*",num2,"=",multiply(num1,num2))

elif choice=="4":
    print(num1,"/",num2,"=",divide(num1,num2))

else:
    print(exit())