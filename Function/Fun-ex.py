# num1 = 10
# num2 = 5

# def addition():
#     add = num1+num2
#     print(add)

# def submittion():
#     sub = num1-num2
#     print(sub)

# def mul():
#     mul = num1*num2
#     print(mul)

# addition()
# submittion()
# mul()

# Function with return Key-Word --- Parameterize Function

def addition(num1, num2):
    add = num1 + num2
    return add

def submittion(num1, num2):
    sub = num1 - num2
    return sub

def multiplication(num1, num2):
    mul = num1 * num2
    return mul

print(addition(10, 5))  # using print because variable values are not define befor, we have to define while calling a function
print(submittion(10, 5))
print(multiplication(10, 5))


