print("welcome to your random name picker")

names = input("enter the names: \n")

names_split = names.split(", ")

import random

guess_num = random.randint (0,len(names_split)-1)


print(f'{names_split[guess_num]} you are to pay for our food. \nthank you.')

