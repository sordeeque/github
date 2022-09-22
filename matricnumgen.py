from datetime import datetime
date = datetime.today().strftime('%Y-%m-%d')
print("welcome to my LCG id generator")
first_name = input("what is your first name: \n")
middle_name = input("what is your middle name: \n")
last_name = input("what is your last name: \n")
DOB = input("what is your date of birth: \n")
state = input("what is you state: \n")
phone_number = input("enter your phone number: \n")

import random
num = random.randint(10000, 99999)
nam = random.randint(1001, 9999)
print("this is your LCG id number. \nNB: make sure to keep from others")
print("First Name: "+first_name)
print("Middle Name: "+middle_name)
print("Last Name: "+last_name)
print("DOB: "+DOB)
print("state: "+state)
print("Date: "+date)
print("Phone Number: "+phone_number+"\n\n")
print("your LCG id is: \n"+str(num)+"/"+state[:2]+"/"+datetime.today().strftime('%Y'))
print("\n Hello! "+first_name+" "+middle_name+" "+last_name)
print("your password and login id :--> \n")
print("your username: \n"+(first_name[:3]+str(nam)))
import secrets
import string
alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(20))
print("your password: /n"+(password))































'''import array
 
# maximum length of password needed
# this can be changed to suit your password length
MAX_LEN = 12
 
# declare arrays of the character that we need in out password
# Represented as chars to enable easy string concatenation
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
 
UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
 
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']
 
# combines all the character arrays above to form one array
COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
 
# randomly select at least one character from each character set above
rand_digit = random.choice(DIGITS)
rand_upper = random.choice(UPCASE_CHARACTERS)
rand_lower = random.choice(LOCASE_CHARACTERS)
rand_symbol = random.choice(SYMBOLS)
 
# combine the character randomly selected above
# at this stage, the password contains only 4 characters but
# we want a 12-character password
temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
 
 
# now that we are sure we have at least one character from each
# set of characters, we fill the rest of
# the password length by selecting randomly from the combined
# list of character above.
for x in range(MAX_LEN - 4):
    temp_pass = temp_pass + random.choice(COMBINED_LIST)
 
    # convert temporary password into array and shuffle to
    # prevent it from having a consistent pattern
    # where the beginning of the password is predictable
    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)
 
# traverse the temporary password array and append the chars
# to form the password
password = ""
for x in temp_pass_list:
        password = password + x
         
# print out password
print(password)
'''


