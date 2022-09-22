print ("welcome to my app")

jss1 = 0
jss2 = 0
jss3 = 0
sss1 = 0
sss2 = 0
sss3 = 0

first_name = input("input your name: \n")
mid_name = input("what is your middle name: \n")
last_name = input("what is your last name: \n")
DOB = input("what is your date of birth: \n")
state = input("what is you state: \n")
phone_number = input("enter your phone number: \n")
sd_class = input("what class are you(jss1/jss2/jss3/sss1/sss2/sss3): \n")
if sd_class == 'jss1':
    jss1 += 10000
    print(f'{first_name} your tuition fee is #{jss1}')
elif sd_class == 'jss2':
    jss2 += 20000
    print(f'{first_name} your tuition fee is #{jss2}')
elif sd_class == 'jss3':
    jss3 += 30000
    print(f'{first_name} your tuition fee is #{jss3}')
elif sd_class == 'sss1':
    sss1 += 40000
    print(f'{first_name} your tuition fee is #{sss1}')
elif sd_class == 'sss2':
    sss2 += 50000
    print(f'{first_name} your tuition fee is #(sss2)')
elif sd_class == 'sss3':
    sss3 += 60000
    print(f'{first_name} your tuition fee is #{sss3}')
else:
    print(f'our school dont allow more than jss and sss class')
                    
