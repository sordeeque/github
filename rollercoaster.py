print("welcome to roller coaster text app")

bill = 5
pic_bill = 15
ice_bill = 10

min_height = int(120)
min_age = int(10)

name = input("enter your name: \n")

height = int(input("enter your height: \n"))

if height >= min_height:
    print("you are elligible. ")

    age = int(input("enter your age: \n"))
    if age >= min_age:
        print("you are elligible. \nyour bill is $"+str(bill))
    else:
        print("you are not elligible. ")
else:
    print("you are not elligible. ")

pic = input("will you like to take picture(Y/N): \n").upper()

if pic == 'Y' and age >= min_height:
    print("thank you!"+name+", your bill is "+"$"+str(bill+pic_bill))

if pic == 'Y' and age != min_height and age < min_height:
    print("thank you!"+name+", your bill is "+"$"+str(pic_bill))    

    col = input("will you collect your pics now(Y/N): \n").upper()
    if col == 'Y':
        print("thanks "+name+".")

    else:
        print("thanks "+name+".")
        

else:
    print("OKAY!"+name+", ")
    

ice = input("will you like some ice cream(Y/N): \n").upper()


if pic == 'Y' and age != min_height and age < min_height and ice == 'N':
    print("thank you!"+name+", your bill is "+"$"+str(pic_bill))

'''if pic == 'Y' and age != min_height and age < min_height and ice == 'Y':
    print("thank you!"+name+", your total bill is "+"$"+str(pic_bill+ice_bill))'''
    

if ice == 'Y' and pic == 'Y' and age >= min_age :
    print("thank you!"+name+", your total bill is "+"$"+str(bill+pic_bill+ice_bill))

else:
    print("thank you!"+name+", have a nice time here")

if ice == 'Y' and pic == 'N' and age >= min_height:
    print("thank you!"+name+", your total bill is "+"$"+str(bill+ice_bill))


if pic == 'Y' and ice == 'N' and age >= min_height:
    print("thank you!"+name+", your total bill is "+"$"+str(bill+pic_bill))
    
    
    
    
    
