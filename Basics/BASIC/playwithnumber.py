num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))

opr = input("enter a operator(like: '+','-','*','%'): ")
output = None # this is using because this will run this code without crashing if user type wrong numbers or operator.


if opr == "+":
    output = num1+num2

if opr == "-":
    output = num1-num2

if opr == "*":
    output = num1*num2

if opr == "/":
    output = num1%num2

print()

print("your calculation is: ",output)

# ELSE-IF Statement Example
if num1 < 5:
    print("num1 is less then 5")

else:
    print("num1 is greter then 5")

# ELIF Statement Example
if num1 < 5:
    print("num1 is less then 5")
elif num1 == 5:
    print("num1 is equal to 5")

else:
    print("num1 is greter then 5")
