'''
def what_is_your_name(name):
    print(f"My name is {name}.")
what_is_your_name("Peter")
what_is_your_name("Benson")
what_is_your_name("Faithful")


def calculator(a, b, c):
    if b == "+":
        result = int(a) + int(c)
    elif b == "-":
        result = int(a) - int(c)
    elif b == "/":
        result = int(a) / int(c)
    else:
        result = int(a) * int(c)
    print(result)

'''
cal_on = True

while cal_on:
    first_num = int(input("Enter a number: "))
    option = input("Choose an option (+,-,/,*): ")
    sec_num = int(input("Enter a number: "))

    calculator(first_num, option, sec_num)


def greetings(name, age):
    print(f"Welcome {name}, You are {age} years old.")

greetings('Peter', 12)
greetings(age=12, name='peter')
